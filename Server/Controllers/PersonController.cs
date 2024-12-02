using Microsoft.AspNetCore.Mvc;
using Server.Handlers.CommandHandlers;
using Server.Handlers.QueryHandlers;
using Server.Models;
using Server.Models.Commands.Person;
using Server.Models.Queries.Person;

namespace Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PersonController : ControllerBase
    {
        private readonly PersonQueryHandler _queryHandler;
        private readonly PersonCommandHandler _commandHandler;

        public PersonController(PersonQueryHandler queryHandler, PersonCommandHandler commandHandler)
        {
            _queryHandler = queryHandler;
            _commandHandler = commandHandler;
        }

        // GET: api/<PersonController>
        [HttpGet]
        public async Task<IActionResult> Get()
        {
            var query = new GetAllPersonsQuery();
            var persons = await _queryHandler.Handle(query);
            return Ok(persons);
        }

        // GET api/<PersonController>/5
        [HttpGet("{id}")]
        public async Task<IActionResult> Get(int id)
        {
            var query = new GetPersonByIdQuery { Id = id };
            var person = await _queryHandler.Handle(query);
            if (person != null)
            {
                return Ok(person);
            }
            return NotFound($"Person with Id = {id} not found");
        }

        // POST api/<PersonController>
        [HttpPost]
        public async Task<IActionResult> Post([FromBody] CreatePersonCommand command)
        {
            if (command == null)
            {
                return BadRequest("Invalid person data.");
            }

            int newPersonId = await _commandHandler.Handle(command);
            if (newPersonId > 0)
            {
                return Ok($"Person created with Id = {newPersonId}");
            }

            return StatusCode(500, "An error occurred while creating the person");
        }

        // PUT api/<PersonController>/5
        [HttpPut("{id}")]
        public async Task<IActionResult> Put(int id, [FromBody] UpdatePersonCommand command)
        {
            if (id != command.Id)
            {
                return BadRequest("Person ID mismatch.");
            }

            int result = await _commandHandler.Handle(command);
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
            var command = new DeletePersonCommand { Id = id };
            int result = await _commandHandler.Handle(command);
            if (result > 0)
            {
                return Ok($"Person with Id = {id} deleted successfully");
            }

            return NotFound($"Person with Id = {id} not found");
        }
    }
}
