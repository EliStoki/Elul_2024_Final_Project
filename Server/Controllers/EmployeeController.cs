using Microsoft.AspNetCore.Mvc;
using Server.Models;
using Server.Models.DA;

namespace Server.Controllers;

[Route("api/[controller]")]
[ApiController]
public class EmployeeController : ControllerBase
{
    private readonly EmployeeDA _employeeDA = new EmployeeDA();

    // GET: api/<EmployeeController>
    [HttpGet]
    public async Task<IActionResult> Get()
    {
        var employees = await _employeeDA.GetAllEmployeesAsync();
        return Ok(employees);
    }

    // GET api/<EmployeeController>/5
    [HttpGet("{id}")]
    public async Task<IActionResult> Get(int id)
    {
        var employee = await _employeeDA.GetEmployeeAsync(id);
        if (employee != null)
        {
            return Ok(employee);
        }
        return NotFound($"Employee with Id = {id} not found");
    }

    // POST api/<EmployeeController>
    [HttpPost]
    public async Task<IActionResult> Post([FromBody] Employee employee)
    {
        if (employee == null)
        {
            return BadRequest("Employee object is null");
        }

        int newEmployeeId = await _employeeDA.CreateEmployeeAsync(employee);
        if (newEmployeeId > 0)
        {
            return Ok($"Employee created with Id = {newEmployeeId}");
        }

        return StatusCode(500, "An error occurred while creating the employee");
    }

    // PUT api/<EmployeeController>/5
    [HttpPut("{id}")]
    public async Task<IActionResult> Put(int id, [FromBody] Employee employee)
    {
        if (id != employee.Id)
        {
            return BadRequest("Employee ID mismatch");
        }

        int result = await _employeeDA.UpdateEmployeeAsync(employee);
        if (result > 0)
        {
            return Ok("Employee updated successfully");
        }

        return NotFound($"Employee with Id = {id} not found");
    }

    // DELETE api/<EmployeeController>/5
    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(int id)
    {
        int result = await _employeeDA.DeleteEmployeeAsync(id);
        if (result > 0)
        {
            return Ok($"Employee with Id = {id} deleted successfully");
        }

        return NotFound($"Employee with Id = {id} not found");
    }
}
