using System.Net.Http.Headers;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using RestSharp;

namespace Server.Services;

public class Coordinates
{
    public int Height { get; set; }
    public int Width { get; set; }
    public int Xmax { get; set; }
    public int Xmin { get; set; }
    public int Ymax { get; set; }
    public int Ymin { get; set; }
}

public class ImaggaService
{
    string apiKey = "acc_1e99b464650d238";
    string apiSecret = "0a3303b80de04c1a955fe5240e217087";
    RestClient client = new RestClient("https://api.imagga.com/v2/faces/detections");

    private readonly HttpClient _httpClient;
    private const string BaseUrl = "https://api.imagga.com/v2/faces/detections";

    public ImaggaService()
    {
        _httpClient = new HttpClient();
    }

    public async Task<string> GetFaceDetectionCropImage(string imageUrl, string userName = "userName")
    {
        string basicAuthValue = System.Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes($"{apiKey}:{apiSecret}"));

        //string imageUrl = "https://imagga.com/static/images/categorization/child-476506_640.jpg";

        // Create request
        var request = new RestRequest();
        request.Method = Method.Get;
        request.AddParameter("image_url", imageUrl);
        request.AddHeader("Authorization", String.Format("Basic {0}", basicAuthValue));

        // Set timeout to 6 seconds
        request.Timeout = TimeSpan.FromSeconds(6);

        // Execute request asynchronously
        RestResponse response = await client.ExecuteAsync(request);

        if(response.IsSuccessful)
            {
            // Deserialize the response content to extract face data
            var json = JObject.Parse(response.Content);
            var faces = json["result"]["faces"];

            if (faces != null && faces.HasValues)
            {
                // Extract coordinates and confidence from the first detected face - get the first face in image
                var face = faces[0];
                var coordinates = face["coordinates"].ToObject<Coordinates>();
                var confidence = face["confidence"].ToObject<double>();

                //Crop image based on face detection
                string imagePath = await ImageCropper.CropImageFromUrl(imageUrl, coordinates.Xmin, coordinates.Ymin, coordinates.Width, coordinates.Height, userName);
                return imagePath;
                //return the image as Json
                //return Convert.ToBase64String(File.ReadAllBytes(imagePath));
            }
            else
            {
                throw new Exception("No face detected in the image.");
            }
        }
        throw new Exception("Not Permitted");
    }
}
