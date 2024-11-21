using System.Data;

namespace Server.Models.DA;

public class PermissionDA
{
    private DataBaseService _databaseService = DataBaseService.GetInstance();

    public PermissionDA() { }

    public async Task<int> CreatePermissionAsync(Permission permission)
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

        return -1;
    }

    public async Task<Permission> GetPermissionAsync(int id)
    {
        string query = $"SELECT * FROM Permission WHERE permission_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            return new Permission(
                Convert.ToInt32(row["floor_level"]),
                row["building"].ToString()
            )
            {
                Id = Convert.ToInt32(row["permission_id"])
            };
        }

        return null;
    }

    public async Task<List<Permission>> GetAllPermissionsAsync()
    {
        string query = "SELECT * FROM Permission";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        var permissions = new List<Permission>();
        foreach (DataRow row in result.Rows)
        {
            permissions.Add(new Permission(
                Convert.ToInt32(row["floor_level"]),
                row["building"].ToString()
            )
            {
                Id = Convert.ToInt32(row["permission_id"])
            });
        }

        return permissions;
    }

    public async Task<int> UpdatePermissionAsync(Permission permission)
    {
        string query = $@"
                UPDATE Permission 
                SET floor_level = {permission.FloorLevel}, building = '{permission.Building}' 
                WHERE permission_id = {permission.Id}";

        return await _databaseService.ExecuteNonQueryAsync(query);
    }

    public async Task<int> DeletePermissionAsync(int id)
    {
        string query = $"DELETE FROM Permission WHERE permission_id = {id}";
        return await _databaseService.ExecuteNonQueryAsync(query);
    }
}
