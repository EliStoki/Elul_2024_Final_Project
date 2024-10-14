using Microsoft.AspNetCore.Mvc;
using Server.Models;
using Server.Models.DA;
using System.Threading.Tasks;

namespace Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PersonController : ControllerBase
    {
        private readonly PersonDA _personDA = new PersonDA();

        // GET: api/<PersonController>
        [HttpGet]
        public async Task<IActionResult> Get()
        {
            var persons = await _personDA.GetAllPersonsAsync();
            return Ok(persons);
        }


        // GET api/<PersonController>/5
        [HttpGet("{id}")]
        public async Task<IActionResult> Get(int id)
        {
            var person = await _personDA.GetPersonAsync(id);
            if (person != null)
            {
                return Ok(person);
            }
            return NotFound($"Person with Id = {id} not found");
        }

        // POST api/<PersonController>
        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Person person)
        {
            if (person == null)
            {
                return BadRequest("Person object is null");
            }

            int newPersonId = await _personDA.CreatePersonAsync(person);
            if (newPersonId > 0)
            {
                //return CreatedAtAction(nameof(Get), new { id = newPersonId }, person);
                return Ok($"id = {newPersonId}");
            }

            return StatusCode(500, "An error occurred while creating the person");
        }

        // PUT api/<PersonController>/5
        [HttpPut("{id}")]
        public async Task<IActionResult> Put(int id, [FromBody] Person person)
        {
            if (id != person.Id)
            {
                return BadRequest("Person ID mismatch");
            }

            int result = await _personDA.UpdatePersonAsync(person);
            if (result > 0)
            {
                return Ok("Person updated successfully");
            }

            return NotFound($"Person with Id = {id} not found");
        }

        // DELETE api/<PersonController>/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            int result = await _personDA.DeletePersonAsync(id);
            if (result > 0)
            {
                return Ok($"Person with Id = {id} deleted successfully");
            }

            return NotFound($"Person with Id = {id} not found");
        }
    }
}
