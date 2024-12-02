using System.Data;
using Server.Models;
using Server.Models.Infrastructure;

namespace Server.Models.DataAccess.Department;

public class DepartmentQuery
{
    private readonly DataBaseService _databaseService;

    public DepartmentQuery()
    {
        _databaseService = DataBaseService.GetInstance();
    }

    // Method to get a department by ID
    public async Task<Server.Models.Department> GetDepartmentAsync(int id)
    {
        string query = $"SELECT * FROM Department WHERE dept_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);
        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            return new Server.Models.Department(
                Convert.ToInt32(row["dept_id"]),
                row["dept_name"].ToString()
            );
        }
        return null;
    }

    // Method to get all departments
    public async Task<List<Server.Models.Department>> GetAllDepartmentsAsync()
    {
        string query = "SELECT * FROM Department";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        var departments = new List<Server.Models.Department>();
        foreach (DataRow row in result.Rows)
        {
            departments.Add(new Server.Models.Department(
                Convert.ToInt32(row["dept_id"]),
                row["dept_name"].ToString()
            ));
        }
        return departments;
    }
}
