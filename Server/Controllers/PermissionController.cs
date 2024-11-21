using Microsoft.AspNetCore.Mvc;
using Server.Models;
using Server.Models.DA;

namespace Server.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PermissionController : ControllerBase
    {
        private readonly PermissionDA _permissionDA = new PermissionDA();

        // GET: api/<PermissionController>
        [HttpGet]
        public async Task<IActionResult> Get()
        {
            var permissions = await _permissionDA.GetAllPermissionsAsync();
            return Ok(permissions);
        }

        // GET api/<PermissionController>/5
        [HttpGet("{id}")]
        public async Task<IActionResult> Get(int id)
        {
            var permission = await _permissionDA.GetPermissionAsync(id);
            if (permission != null)
            {
                return Ok(permission);
            }
            return NotFound($"Permission with Id = {id} not found");
        }

        // POST api/<PermissionController>
        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Permission permission)
        {
            if (permission == null)
            {
                return BadRequest("Permission object is null");
            }

            int newPermissionId = await _permissionDA.CreatePermissionAsync(permission);
            if (newPermissionId > 0)
            {
                return Ok($"Permission created with Id = {newPermissionId}");
            }

            return StatusCode(500, "An error occurred while creating the permission");
        }

        // PUT api/<PermissionController>/5
        [HttpPut("{id}")]
        public async Task<IActionResult> Put(int id, [FromBody] Permission permission)
        {
            if (id != permission.Id)
            {
                return BadRequest("Permission ID mismatch");
            }

            int result = await _permissionDA.UpdatePermissionAsync(permission);
            if (result > 0)
            {
                return Ok("Permission updated successfully");
            }

            return NotFound($"Permission with Id = {id} not found");
        }

        // DELETE api/<PermissionController>/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            int result = await _permissionDA.DeletePermissionAsync(id);
            if (result > 0)
            {
                return Ok($"Permission with Id = {id} deleted successfully");
            }

            return NotFound($"Permission with Id = {id} not found");
        }
    }
}
