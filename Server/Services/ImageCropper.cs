using OpenCvSharp;

namespace Server.Services;

public static class ImageCropper
{
    /// <summary>
    /// Crops an image based on the specified coordinates and dimensions using OpenCV.
    /// </summary>
    /// <param name="imageUrl">The url to the original image.</param>
    /// <param name="x">The X-coordinate of the top-left corner.</param>
    /// <param name="y">The Y-coordinate of the top-left corner.</param>
    /// <param name="width">The width of the cropped image.</param>
    /// <param name="height">The height of the cropped image.</param>
    /// <param name="picName" "The picture name without the file type"></param>
    public static async Task<string> CropImageFromUrl(string imageUrl, int x, int y, int width, int height, string picName)
    {
        // Download the image from the URL
        byte[] imageData = await DownloadImageFromUrlAsync(imageUrl);

        // Load the image into an OpenCV Mat object from the byte array
        Mat originalImage = Cv2.ImDecode(imageData, ImreadModes.Color);

        // Ensure the cropping rectangle is within the bounds of the image
        if (x < 0 || y < 0 || x + width > originalImage.Width || y + height > originalImage.Height)
        {
            throw new ArgumentException("The cropping area exceeds the boundaries of the image.");
        }

        // Define the rectangle for cropping
        Rect cropRect = new Rect(x, y, width, height);

        // Crop the image
        Mat croppedImage = new Mat(originalImage, cropRect);

        // Save the cropped image to the temp directory
        string tempPath = Path.GetTempPath(); // OS temp directory
        string outputImagePath = Path.Combine(tempPath, $"{picName}.jpg");
        Cv2.ImWrite(outputImagePath, croppedImage);

        // Release resources
        originalImage.Dispose();
        croppedImage.Dispose();

        return outputImagePath;
    }

    /// <summary>
    /// Downloads image data from the given URL.
    /// </summary>
    /// <param name="imageUrl">The URL of the image.</param>
    /// <returns>A byte array containing the image data.</returns>
    private static async Task<byte[]> DownloadImageFromUrlAsync(string imageUrl)
    {
        using (HttpClient client = new HttpClient())
        {
            HttpResponseMessage response = await client.GetAsync(imageUrl);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsByteArrayAsync();
        }
    }


}


