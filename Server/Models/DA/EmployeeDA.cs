using System.Data;

namespace Server.Models.DA
{
    public class EmployeeDA
    {
        private DataBaseService _databaseService = DataBaseService.GetInstance();
        private DepartmentDA departmentDA = new();
        private PermissionDA permissionDA = new();
        private PersonDA personDA = new();
        public EmployeeDA() { }

        public async Task<int> CreateEmployeeAsync(Employee employee) //TO DO - create automatic person + convert image to url....
        {
            string query = $@"
                INSERT INTO Employee (Name, Age, Address, Position, DepartmentId, ImageUrl, PermissionId)
                VALUES ('{employee.Name}', {employee.Age}, '{employee.Address}', '{employee.Position}', {employee.Department.Id}, '{employee.ImageUrl}', {employee.Permission.Id});
                SELECT SCOPE_IDENTITY();";

            DataTable result = await _databaseService.ExecuteQueryAsync(query);

            if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
            {
                return Convert.ToInt32(result.Rows[0][0]);
            }

            return -1;
        }


        public async Task<Employee> GetEmployeeAsync(int id)
        {
            // Query to get the employee
            string query = $"SELECT * FROM Employee WHERE employee_id = {id}";
            DataTable result = await _databaseService.ExecuteQueryAsync(query);

            if (result.Rows.Count > 0)
            {
                DataRow row = result.Rows[0];

                // Extract department and permission IDs from the employee table
                int departmentId = Convert.ToInt32(row["dept_id"]);
                int permissionId = Convert.ToInt32(row["permission_id"]);
                int personId = Convert.ToInt32(row["person_id"]);

                // Fetch department and permission asynchronously
                var departmentTask = departmentDA.GetDepartmentAsync(departmentId);
                var permissionTask = permissionDA.GetPermissionAsync(permissionId);
                var personTask = personDA.GetPersonAsync(personId);

                // Await both tasks
                var department = await departmentTask;
                var permission = await permissionTask;
                var person = await personTask;

                // Create the employee object
                return new Employee(
                    person.Name,
                    person.Age,
                    person.Address,
                    Convert.ToInt32(row["employee_id"]),
                    row["Position"].ToString(),
                    department,
                    row["image_url"].ToString(),
                    permission
                );
            }

            return null;
        }


        public async Task<List<Employee>> GetAllEmployeesAsync()
        {
            string query = "SELECT * FROM Employee";
            DataTable result = await _databaseService.ExecuteQueryAsync(query);

            var employees = new List<Employee>();

            foreach (DataRow row in result.Rows)
            {
                // Extract foreign key IDs for Department and Permission
                int departmentId = Convert.ToInt32(row["DepartmentId"]);
                int permissionId = Convert.ToInt32(row["PermissionId"]);
                int personId = Convert.ToInt32(row["person_id"]);

                // Fetch the Department and Permission objects asynchronously
                var departmentTask = departmentDA.GetDepartmentAsync(departmentId);
                var permissionTask = permissionDA.GetPermissionAsync(permissionId);
                var personTask = personDA.GetPersonAsync(personId);

                var department = await departmentTask;
                var permission = await permissionTask;
                var person = await personTask;

                // Add the employee to the list
                employees.Add(new Employee(
                    person.Name,
                    person.Age,
                    person.Address,
                    Convert.ToInt32(row["employee_id"]),
                    row["Position"].ToString(),
                    department,
                    row["image_url"].ToString(),
                    permission
                ));
            }

            return employees;
        }


        public async Task<int> UpdateEmployeeAsync(Employee employee)
        {
            string query = $@"
                UPDATE Employee 
                SET Name = '{employee.Name}', Age = {employee.Age}, Address = '{employee.Address}', 
                    Position = '{employee.Position}', DepartmentId = {employee.Department.Id}, 
                    ImageUrl = '{employee.ImageUrl}', PermissionId = {employee.Permission.Id}
                WHERE employee_id = {employee.Id}";

            return await _databaseService.ExecuteNonQueryAsync(query);
        }

        public async Task<int> DeleteEmployeeAsync(int id)
        {
            string query = $"DELETE FROM Employee WHERE employee_id = {id}";
            return await _databaseService.ExecuteNonQueryAsync(query);
        }
    }
}
