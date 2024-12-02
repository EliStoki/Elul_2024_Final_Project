using Google.Cloud.Storage.V1;
using System;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;

namespace Server.Services
{
    public class GoogleCloudStorageService
    {
        private readonly StorageClient _storageClient;
        private const string BucketName = "mybox1996"; // Replace with your bucket name

        public GoogleCloudStorageService()
        {
            _storageClient = StorageClient.Create();
        }

        public async Task<string> UploadFileAsync(Stream fileStream, string fileName, string contentType)
        {
            try
            {
                await _storageClient.UploadObjectAsync(
                    BucketName,
                    fileName,
                    contentType,
                    fileStream
                );

                // Generate a signed URL with public read access
                var urlSigner = UrlSigner.FromCredential(Google.Apis.Auth.OAuth2.GoogleCredential.GetApplicationDefault());
                var expiration = TimeSpan.FromDays(7); // Long expiration for public access

                return urlSigner.Sign(
                    BucketName,
                    fileName,
                    expiration,
                    HttpMethod.Get
                );
            }
            catch (Exception ex)
            {
                throw new Exception($"Failed to upload file: {ex.Message}", ex);
            }
        }
    }
}
