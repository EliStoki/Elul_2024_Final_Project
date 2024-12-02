using Microsoft.AspNetCore.Mvc;
using Server.Handlers.CommandHandlers;
using Server.Handlers.QueryHandlers;
using Server.Models.Commands.Permission;
using Server.Models.Queries.Permission;

[ApiController]
[Route("api/[controller]")]
public class PermissionController : ControllerBase
{
    private readonly PermissionCommandHandler _commandHandler;
    private readonly PermissionQueryHandler _queryHandler;

    public PermissionController(PermissionCommandHandler commandHandler, PermissionQueryHandler queryHandler)
    {
        _commandHandler = commandHandler;
        _queryHandler = queryHandler;
    }

    // GET: api/Permission
    [HttpGet]
    public async Task<IActionResult> Get()
    {
        var query = new GetAllPermissionsQuery();
        var permissions = await _queryHandler.Handle(query);
        return Ok(permissions);
    }

    // GET: api/Permission/5
    [HttpGet("{id}")]
    public async Task<IActionResult> Get(int id)
    {
        var query = new GetPermissionByIdQuery { Id = id };
        var permission = await _queryHandler.Handle(query);
        if (permission == null)
        {
            return NotFound($"Permission with Id = {id} not found.");
        }
        return Ok(permission);
    }

    // POST: api/Permission
    [HttpPost]
    public async Task<IActionResult> Post([FromBody] CreatePermissionCommand command)
    {
        if (command == null)
        {
            return BadRequest("Invalid permission data.");
        }

        int newPermissionId = await _commandHandler.Handle(command);
        return Ok($"Permission created with Id = {newPermissionId}");
    }

    // PUT: api/Permission/5
    [HttpPut("{id}")]
    public async Task<IActionResult> Put(int id, [FromBody] UpdatePermissionCommand command)
    {
        if (id != command.Id)
        {
            return BadRequest("Permission ID mismatch.");
        }

        int result = await _commandHandler.Handle(command);
        if (result > 0)
        {
            return Ok("Permission updated successfully.");
        }

        return NotFound($"Permission with Id = {id} not found.");
    }

    // DELETE: api/Permission/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(int id)
    {
        var command = new DeletePermissionCommand { Id = id };
        int result = await _commandHandler.Handle(command);
        if (result > 0)
        {
            return Ok($"Permission with Id = {id} deleted successfully.");
        }

        return NotFound($"Permission with Id = {id} not found.");
    }
}
