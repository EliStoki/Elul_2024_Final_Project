using Microsoft.AspNetCore.Mvc;
using Server.Models;
using Server.Models.DA;

namespace Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class DepartmentController : ControllerBase
    {
        private readonly DepartmentDA _departmentDA = new DepartmentDA();

        // GET: api/<DepartmentController>
        [HttpGet]
        public async Task<IActionResult> Get()
        {
            var departments = await _departmentDA.GetAllDepartmentsAsync();
            return Ok(departments);
        }

        // GET api/<DepartmentController>/5
        [HttpGet("{id}")]
        public async Task<IActionResult> Get(int id)
        {
            var department = await _departmentDA.GetDepartmentAsync(id);
            if (department != null)
            {
                return Ok(department);
            }
            return NotFound($"Department with Id = {id} not found");
        }

        // POST api/<DepartmentController>
        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Department department)
        {
            if (department == null)
            {
                return BadRequest("Department object is null");
            }

            int newDeptId = await _departmentDA.CreateDepartmentAsync(department);
            if (newDeptId > 0)
            {
                return Ok($"Department created with Id = {newDeptId}");
            }

            return StatusCode(500, "An error occurred while creating the department");
        }

        // PUT api/<DepartmentController>/5
        [HttpPut("{id}")]
        public async Task<IActionResult> Put(int id, [FromBody] Department department)
        {
            if (id != department.Id)
            {
                return BadRequest("Department ID mismatch");
            }

            int result = await _departmentDA.UpdateDepartmentAsync(department);
            if (result > 0)
            {
                return Ok("Department updated successfully");
            }

            return NotFound($"Department with Id = {id} not found");
        }

        // DELETE api/<DepartmentController>/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            int result = await _departmentDA.DeleteDepartmentAsync(id);
            if (result > 0)
            {
                return Ok($"Department with Id = {id} deleted successfully");
            }

            return NotFound($"Department with Id = {id} not found");
        }
    }
}
