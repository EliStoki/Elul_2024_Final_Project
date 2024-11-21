using Google.Apis.Storage.v1.Data;
using Google.Cloud.Storage.V1;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Server.Services;
using System;
using System.IO;
using System.Threading.Tasks;

namespace Server.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class CloudStorageController : ControllerBase
    {
        private const string BucketName = "mybox1996"; // Replace with your bucket name
        private readonly StorageClient _storageClient;
        private readonly ImaggaService _imaggaService;
        public CloudStorageController()
        {
            // Initialize the Google Cloud Storage client
            _storageClient = StorageClient.Create();
            _imaggaService = new();
        }

        [HttpPost("upload")]
        public async Task<IActionResult> UploadFile([FromForm] IFormFile file, string contentType)
        {

            if (file == null || file.Length == 0)
                return BadRequest("No file uploaded.");

            try
            {
                // Generate a unique file name
                var fileName = Path.GetRandomFileName();

                // Upload the file to the bucket
                using (var stream = file.OpenReadStream())
                {
                    await _storageClient.UploadObjectAsync(
                        BucketName,
                        fileName,
                        contentType,
                        stream
                    );
                }

                // Generate a signed URL with public read access
                UrlSigner urlSigner = UrlSigner.FromCredential(Google.Apis.Auth.OAuth2.GoogleCredential.GetApplicationDefault());
                TimeSpan expiration = TimeSpan.FromDays(7); // Very long expiration for public access
                string publicUrl = urlSigner.Sign(
                    BucketName,
                    fileName,
                    expiration,
                    HttpMethod.Get
                );

                return Ok(new { FileName = fileName, Url = publicUrl });
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Error: {ex.Message}");
            }
        }

        [HttpPost("upload-image")]
        public async Task<IActionResult> UploadImage([FromForm] IFormFile file, string userName = "noname")
        {
            if (file == null || file.Length == 0)
                return BadRequest("No file uploaded.");

            // Check if the file is of type image/*
            if (!file.ContentType.StartsWith("image/"))
            {
                return BadRequest("Only image files are allowed.");
            }

            var result = await UploadFile(file, file.ContentType) as OkObjectResult;

            if (result == null)
            {
                // Handle error case
                return StatusCode(500, "Error uploading file.");
            }

            // Extract the URL from the result
            var fileData = result.Value as dynamic;
            string imageUrl = fileData?.Url;


            var cropImagePath = await _imaggaService.GetFaceDetectionCropImageUrl(imageUrl, userName);

            var fileCropped = CreateIFormFileFromPath(cropImagePath);
            // Further processing with the imageUrl (e.g., save to database, etc.)

            return await UploadFile(fileCropped, file.ContentType);
        }

        private static IFormFile CreateIFormFileFromPath(string filePath)
        {
            var fileInfo = new FileInfo(filePath);
            var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);

            // Create an IFormFile instance
            var formFile = new FormFile(fileStream, 0, fileInfo.Length, "file", fileInfo.Name)
            {
                Headers = new HeaderDictionary(),
                ContentType = "application/octet-stream" // Set the content type as needed
            };

            return formFile;
        }

    }
}
