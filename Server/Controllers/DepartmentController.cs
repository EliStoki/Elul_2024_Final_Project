using Microsoft.AspNetCore.Mvc;
using Server.Commands.Department;
using Server.Handlers.CommandHandlers;
using Server.Handlers.QueryHandlers;
using Server.Queries.Department;
using Server.Queries;

[ApiController]
[Route("api/[controller]")]
public class DepartmentController : ControllerBase
{
    private readonly DepartmentCommandHandler _commandHandler;
    private readonly DepartmentQueryHandler _queryHandler;

    public DepartmentController(DepartmentCommandHandler commandHandler, DepartmentQueryHandler queryHandler)
    {
        _commandHandler = commandHandler;
        _queryHandler = queryHandler;
    }

    // GET: api/Department
    [HttpGet]
    public async Task<IActionResult> Get()
    {
        var query = new GetAllDepartmentsQuery();
        var departments = await _queryHandler.Handle(query);
        return Ok(departments);
    }

    // GET: api/Department/5
    [HttpGet("{id}")]
    public async Task<IActionResult> Get(int id)
    {
        var query = new GetDepartmentByIdQuery { Id = id };
        var department = await _queryHandler.Handle(query);
        if (department == null)
        {
            return NotFound($"Department with Id = {id} not found.");
        }
        return Ok(department);
    }

    // POST: api/Department
    [HttpPost]
    public async Task<IActionResult> Post([FromBody] CreateDepartmentCommand command)
    {
        if (command == null)
        {
            return BadRequest("Invalid department data.");
        }

        int newDeptId = await _commandHandler.Handle(command);
        return Ok($"Department created with Id = {newDeptId}");
    }

    // PUT: api/Department/5
    [HttpPut("{id}")]
    public async Task<IActionResult> Put(int id, [FromBody] UpdateDepartmentCommand command)
    {
        if (id != command.Id)
        {
            return BadRequest("Department ID mismatch.");
        }

        int result = await _commandHandler.Handle(command);
        if (result > 0)
        {
            return Ok("Department updated successfully.");
        }

        return NotFound($"Department with Id = {id} not found.");
    }

    // DELETE: api/Department/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(int id)
    {
        var command = new DeleteDepartmentCommand { Id = id };
        int result = await _commandHandler.Handle(command);
        if (result > 0)
        {
            return Ok($"Department with Id = {id} deleted successfully.");
        }

        return NotFound($"Department with Id = {id} not found.");
    }
}
