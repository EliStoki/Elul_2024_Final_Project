using System.Net.Http.Headers;
using Newtonsoft.Json.Linq;

namespace Server.Services;

public class ImaggaService
{
    private readonly HttpClient _httpClient;
    private const string BaseUrl = "https://api.imagga.com/v2/face/detect";

    public ImaggaService()
    {
        _httpClient = new HttpClient();
    }

    public async Task<string> GetSingleFaceImageAsync(string imageUrl)
    {
        // Set the necessary headers
        var request = new HttpRequestMessage(HttpMethod.Get, $"{BaseUrl}?url={imageUrl}");
        var authToken = Convert.ToBase64String(System.Text.Encoding.ASCII.GetBytes("YOUR_API_KEY:YOUR_API_SECRET"));
        request.Headers.Authorization = new AuthenticationHeaderValue("Basic", authToken);

        // Send the request
        HttpResponseMessage response = await _httpClient.SendAsync(request);
        if (response.IsSuccessStatusCode)
        {
            var responseContent = await response.Content.ReadAsStringAsync();

            // Parse the response content to get the face image URL
            var json = JObject.Parse(responseContent);
            var faceImages = json["result"]["faces"];

            if (faceImages != null && faceImages.HasValues)
            {
                // Assuming we want the first detected face image
                string faceImageUrl = faceImages[0]["face_image_url"].ToString();
                return faceImageUrl;
            }
            else
            {
                throw new Exception("No face detected in the image.");
            }
        }

        throw new Exception($"Imagga API error: {response.ReasonPhrase}");
    }
}
