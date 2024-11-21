using System.Data;

namespace Server.Models.DA;

public class DepartmentDA
{
    private DataBaseService _databaseService = DataBaseService.GetInstance();

    public DepartmentDA() { }

    // Method to create a new department
    public async Task<int> CreateDepartmentAsync(Department department)
    {
        
            string query = $"INSERT INTO Department (dept_name) VALUES ('{department.DeptName}'); " +
                            "SELECT SCOPE_IDENTITY();";

            DataTable result = await _databaseService.ExecuteQueryAsync(query);

            if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
            {
                int newDeptId = Convert.ToInt32(result.Rows[0][0]);
                return newDeptId;
            }

        throw new Exception($"Cannot create new department element");
    }

    // Method to get a department by ID
    public async Task<Department> GetDepartmentAsync(int id)
    {
        string query = $"SELECT * FROM Department WHERE dept_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);
        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            Department department = new Department(
                Convert.ToInt32(row["dept_id"]),
                row["dept_name"].ToString()
            );
            return department;
        }
        return null;
    }

    // Method to get all departments
    public async Task<List<Department>> GetAllDepartmentsAsync()
    {
        string query = "SELECT * FROM Department";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        List<Department> departments = new List<Department>();

        foreach (DataRow row in result.Rows)
        {
            Department department = new Department(
                Convert.ToInt32(row["dept_id"]),
                row["dept_name"].ToString()
            );
            departments.Add(department);
        }

        return departments;
    }

    // Method to update a department
    public async Task<int> UpdateDepartmentAsync(Department department)
    {
        string query = $"UPDATE Department SET dept_name = '{department.DeptName}' WHERE dept_id = {department.Id}";
        int affectedRows = await _databaseService.ExecuteNonQueryAsync(query);
        return affectedRows;
    }

    // Method to delete a department
    public async Task<int> DeleteDepartmentAsync(int deptId) // TO DO - check delete of department in use
    {
        // Check for employees in the department
        string checkQuery = $"SELECT EmployeeId FROM Employee WHERE dept_id = {deptId}";
        DataTable employeeCheckResult = await _databaseService.ExecuteQueryAsync(checkQuery);

        if (employeeCheckResult.Rows.Count > 0)
        {
            // Collect employee IDs
            List<int> employeeIds = new List<int>();
            foreach (DataRow row in employeeCheckResult.Rows)
            {
                employeeIds.Add(Convert.ToInt32(row["EmployeeId"])); // Adjust column name if needed
            }

            // Throw an exception with a message about the employees
            string employeeIdsString = string.Join(", ", employeeIds);
            throw new InvalidOperationException($"An employee is part of the department. Before deleting this, change the employee's department. Employee IDs: {employeeIdsString}");
        }

        // If no employees are found, proceed to delete
        string deleteQuery = $"DELETE FROM Department WHERE dept_id = {deptId}";
        int affectedRows = await _databaseService.ExecuteNonQueryAsync(deleteQuery);
        return affectedRows;
    }
    
}


