namespace Server.Models.DataAccess.Employee;
using System.Data;
using Server.Models.DataAccess.Department;
using Server.Models.DataAccess.Permission;
using Server.Models.DataAccess.Person;
using Server.Models.Infrastructure;

public class EmployeeQuery
{
    private readonly DataBaseService _databaseService;
    private readonly DepartmentQuery _departmentQuery;
    private readonly PermissionQuery _permissionQuery;
    private readonly PersonQuery _personQuery;

    public EmployeeQuery()
    {
        _databaseService = DataBaseService.GetInstance();
        _departmentQuery = new DepartmentQuery();
        _permissionQuery = new PermissionQuery();
        _personQuery = new PersonQuery();
    }

    // Method to get an employee by ID
    public async Task<Models.Employee> GetEmployeeAsync(int id)
    {
        string query = $"SELECT * FROM Employee WHERE employee_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];

            int departmentId = Convert.ToInt32(row["dept_id"]);
            int permissionId = Convert.ToInt32(row["permission_id"]);
            int personId = Convert.ToInt32(row["person_id"]);

            var department = await _departmentQuery.GetDepartmentAsync(departmentId);
            var permission = await _permissionQuery.GetPermissionAsync(permissionId);
            var person = await _personQuery.GetPersonAsync(personId);

            return new Models.Employee(
                person.Name,
                person.Age,
                person.Address,
                Convert.ToInt32(row["employee_id"]),
                row["Position"].ToString(),
                department.Id,
                row["image_url"].ToString(),
                permission.Id
            );
        }

        return null;
    }

    // Method to get all employees
    public async Task<List<Models.Employee>> GetAllEmployeesAsync()
    {
        string query = "SELECT * FROM Employee";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        var employees = new List<Models.Employee>();

        foreach (DataRow row in result.Rows)
        {
            int departmentId = Convert.ToInt32(row["dept_id"]);
            int permissionId = Convert.ToInt32(row["permission_id"]);
            int personId = Convert.ToInt32(row["person_id"]);

            var department = await _departmentQuery.GetDepartmentAsync(departmentId);
            var permission = await _permissionQuery.GetPermissionAsync(permissionId);
            var person = await _personQuery.GetPersonAsync(personId);

            employees.Add(new Models.Employee(
                person.Name,
                person.Age,
                person.Address,
                Convert.ToInt32(row["employee_id"]),
                row["Position"].ToString(),
                department.Id,
                row["image_url"].ToString(),
                permission.Id
            ));
        }

        return employees;
    }
}


