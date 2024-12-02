using Server.Models.Infrastructure;
using System.Data;

namespace Server.Models.DataAccess.Permission;

public class PermissionQuery
{
    private readonly DataBaseService _databaseService;

    public PermissionQuery()
    {
        _databaseService = DataBaseService.GetInstance();
    }

    // Method to get a permission by ID
    public async Task<Models.Permission> GetPermissionAsync(int id)
    {
        string query = $"SELECT * FROM Permission WHERE permission_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            return new Models.Permission(
                Convert.ToInt32(row["permission_id"]),
                Convert.ToInt32(row["floor_level"]),
                row["building"].ToString()
            );
        }

        return null;
    }

    // Method to get all permissions
    public async Task<List<Models.Permission>> GetAllPermissionsAsync()
    {
        string query = "SELECT * FROM Permission";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        List<Models.Permission> permissions = new List<Models.Permission>();

        foreach (DataRow row in result.Rows)
        {
            permissions.Add(new Models.Permission(
                Convert.ToInt32(row["permission_id"]),
                Convert.ToInt32(row["floor_level"]),
                row["building"].ToString()
            ));
        }

        return permissions;
    }
}
