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
    public class ImaggaServiceController : ControllerBase
    {
        // GET: api/<ImaggaServiceController>
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/<ImaggaServiceController>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/<ImaggaServiceController>
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/<ImaggaServiceController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<ImaggaServiceController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}




namespace YourNamespace.Controllers
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

        [HttpPost("get-face-image")]
        public async Task<IActionResult> GetFaceImage([FromBody] string imageUrl)
        {
            if (string.IsNullOrEmpty(imageUrl))
            {
                return BadRequest("Image URL cannot be null or empty.");
            }

            try
            {
                string faceImageUrl = await _imaggaService.GetSingleFaceImageAsync(imageUrl);

                // Fetch the image from the URL
                using var httpClient = new HttpClient();
                var imageResponse = await httpClient.GetAsync(faceImageUrl);

                if (!imageResponse.IsSuccessStatusCode)
                {
                    return NotFound("Face image not found.");
                }

                var imageBytes = await imageResponse.Content.ReadAsByteArrayAsync();

                // Return the image as a file result
                return File(imageBytes, "image/jpeg"); // Change the content type if necessary
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Internal server error: {ex.Message}");
            }
        }
    }
}

