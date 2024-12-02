using System.Data;
using Server.Models;
using Server.Models.Infrastructure;

namespace Server.Models.DataAccess.Department;

public class DepartmentCommand
{
    private readonly DataBaseService _databaseService;

    public DepartmentCommand()
    {
        _databaseService = DataBaseService.GetInstance();
    }

    // Method to create a new department
    public async Task<int> CreateDepartmentAsync(Server.Models.Department department)
    {
        string query = $@"
                INSERT INTO Department (dept_name) 
                VALUES ('{department.DeptName}');
                SELECT SCOPE_IDENTITY();";

        DataTable result = await _databaseService.ExecuteQueryAsync(query);
        if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
        {
            return Convert.ToInt32(result.Rows[0][0]);
        }
        throw new Exception("Cannot create new department element");
    }

    // Method to update a department
    public async Task<int> UpdateDepartmentAsync(Server.Models.Department department)
    {
        string query = $@"
                UPDATE Department 
                SET dept_name = '{department.DeptName}' 
                WHERE dept_id = {department.Id}";

        return await _databaseService.ExecuteNonQueryAsync(query);
    }

    // Method to delete a department
    public async Task<int> DeleteDepartmentAsync(int deptId)
    {
        // Check for employees in the department
        string checkQuery = $@"
                SELECT EmployeeId 
                FROM Employee 
                WHERE dept_id = {deptId}";

        DataTable employeeCheckResult = await _databaseService.ExecuteQueryAsync(checkQuery);
        if (employeeCheckResult.Rows.Count > 0)
        {
            var employeeIds = new List<int>();
            foreach (DataRow row in employeeCheckResult.Rows)
            {
                employeeIds.Add(Convert.ToInt32(row["EmployeeId"]));
            }

            string employeeIdsString = string.Join(", ", employeeIds);
            throw new InvalidOperationException($@"
                    Employees are still part of the department. 
                    Update or reassign the following employees before deleting: {employeeIdsString}");
        }

        // If no employees are found, proceed to delete
        string deleteQuery = $"DELETE FROM Department WHERE dept_id = {deptId}";
        return await _databaseService.ExecuteNonQueryAsync(deleteQuery);
    }
}
