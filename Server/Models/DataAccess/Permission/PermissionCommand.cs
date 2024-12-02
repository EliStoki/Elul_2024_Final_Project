using Server.Models.Infrastructure;
using System.Data;

namespace Server.Models.DataAccess.Permission;

public class PermissionCommand
{
    private readonly DataBaseService _databaseService;

    public PermissionCommand()
    {
        _databaseService = DataBaseService.GetInstance();
    }

    // Method to create a new permission
    public async Task<int> CreatePermissionAsync(Models.Permission permission)
    {
        string query = $@"
                INSERT INTO Permission (floor_level, building) 
                VALUES ({permission.FloorLevel}, '{permission.Building}');
                SELECT SCOPE_IDENTITY();";

        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
        {
            return Convert.ToInt32(result.Rows[0][0]);
        }

        throw new Exception("Cannot create new permission element");
    }

    // Method to update a permission
    public async Task<int> UpdatePermissionAsync(Models.Permission permission)
    {
        string query = $@"
                UPDATE Permission 
                SET floor_level = {permission.FloorLevel}, building = '{permission.Building}' 
                WHERE permission_id = {permission.Id}";

        return await _databaseService.ExecuteNonQueryAsync(query);
    }

    // Method to delete a permission
    public async Task<int> DeletePermissionAsync(int permissionId)
    {
        string deleteQuery = $"DELETE FROM Permission WHERE permission_id = {permissionId}";
        return await _databaseService.ExecuteNonQueryAsync(deleteQuery);
    }
}
