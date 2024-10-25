using System.Data;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Server.Models.DA;

public class PermissionDA
{
    private DataBaseService _databaseService = DataBaseService.GetInstance();

    public PermissionDA() { }

    // Method to create a new permission
    public async Task<int> CreatePermissionAsync(Permission permission)
    {
        string query = $"INSERT INTO Permission (floor_level, building) VALUES ({permission.FloorLevel}, '{permission.Building}'); " +
                        "SELECT SCOPE_IDENTITY();";

        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
        {
            int newPermissionId = Convert.ToInt32(result.Rows[0][0]);
            return newPermissionId;
        }

        throw new Exception("Cannot create new permission element");
    }

    // Method to get a permission by ID
    public async Task<Permission> GetPermissionAsync(int id)
    {
        string query = $"SELECT * FROM Permission WHERE permission_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);
        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            Permission permission = new Permission(
                Convert.ToInt32(row["permission_id"]),
                Convert.ToInt32(row["floor_level"]),
                row["building"].ToString()
            );
            return permission;
        }
        return null;
    }

    // Method to get all permissions
    public async Task<List<Permission>> GetAllPermissionsAsync()
    {
        string query = "SELECT * FROM Permission";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        List<Permission> permissions = new List<Permission>();

        foreach (DataRow row in result.Rows)
        {
            Permission permission = new Permission(
                Convert.ToInt32(row["permission_id"]),
                Convert.ToInt32(row["floor_level"]),
                row["building"].ToString()
            );
            permissions.Add(permission);
        }

        return permissions;
    }

    // Method to update a permission
    public async Task<int> UpdatePermissionAsync(Permission permission)
    {
        string query = $"UPDATE Permission SET floor_level = {permission.FloorLevel}, building = '{permission.Building}' WHERE permission_id = {permission.Id}";
        int affectedRows = await _databaseService.ExecuteNonQueryAsync(query);
        return affectedRows;
    }

    // Method to delete a permission
    public async Task<int> DeletePermissionAsync(int permissionId)
    {
        string deleteQuery = $"DELETE FROM Permission WHERE permission_id = {permissionId}";
        int affectedRows = await _databaseService.ExecuteNonQueryAsync(deleteQuery);
        return affectedRows;
    }
}
