using Microsoft.AspNetCore.Mvc;
using Server.Services;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Threading.Tasks;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FaceImageController : ControllerBase
    {
        private readonly ImaggaService _imaggaService;

        public FaceImageController()
        {
            _imaggaService = new ImaggaService();
        }

        [HttpGet("get-face-image")]
        public async Task<IActionResult> GetFaceImage()
        {
            try
            {
                // Call your service to get the cropped image path (on the server)
                string imagePath = await _imaggaService.GetFaceDetectionCropImage();

                // Ensure the image exists
                if (!System.IO.File.Exists(imagePath))
                {
                    return NotFound("Face image not found.");
                }

                // Read the image bytes
                var imageBytes = await System.IO.File.ReadAllBytesAsync(imagePath);

                // Get the image filename (optional, you can set a default filename as well)
                var fileName = System.IO.Path.GetFileName(imagePath);

                // Set the Content-Disposition header to force a download
                Response.Headers.Add("Content-Disposition", $"attachment; filename={fileName}");

                // Return the image as a file result with appropriate content type
                return File(imageBytes, "image/jpeg"); // Adjust the content type as needed (e.g., "image/png")
            }
            catch (Exception ex)
            {
                // Log the error and return a 500 status code in case of an internal server error
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }


        [HttpGet("get-face-image-multipart")]
        public async Task<IActionResult> GetFaceImageAsMultipart()
        {
            try
            {
                // Call your service to get the cropped image path (on the server)
                string imagePath = await _imaggaService.GetFaceDetectionCropImage();

                // Ensure the image exists
                if (!System.IO.File.Exists(imagePath))
                {
                    return NotFound(new { message = "Face image not found." });
                }

                // Read the image bytes
                var imageBytes = await System.IO.File.ReadAllBytesAsync(imagePath);

                // Get the image filename (optional, you can set a default filename as well)
                var fileName = System.IO.Path.GetFileName(imagePath);

                // Create a multipart/form-data response
                var stream = new MemoryStream(imageBytes);
                var content = new MultipartFormDataContent();

                // Add the image to the multipart content
                var fileContent = new StreamContent(stream);
                fileContent.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("image/jpeg"); // Adjust the content type if needed
                content.Add(fileContent, "file", fileName);

                // Send the multipart response
                return new FileStreamResult(stream, "multipart/form-data")
                {
                    FileDownloadName = fileName
                };
            }
            catch (Exception ex)
            {
                // Log the error and return a 500 status code in case of an internal server error
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }


    }
}

