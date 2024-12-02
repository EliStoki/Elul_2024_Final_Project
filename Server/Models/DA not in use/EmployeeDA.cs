using System.Data;
using System.Xml.Linq;
using Server.Infrastructure;
using Server.Services;

namespace Server.Models.DA
{
    public class EmployeeDA
    {
        private DataBaseService _databaseService = DataBaseService.GetInstance();
        private GoogleCloudStorageService _googleCloudStorageService = new();
        private ImaggaService _imaggaService = new();

        private DepartmentDA departmentDA = new();
        private PermissionDA permissionDA = new();
        private PersonDA personDA = new();

        public EmployeeDA() { }

        public async Task<int> CreateEmployeeAsync(Employee employee, IFormFile file)
        {

            Person person = new(employee.Name, employee.Age, employee.Address);
            var personId = await personDA.CreatePersonAsync(person);

            var perm = await permissionDA.GetPermissionAsync(employee.Permission);
            var dept = await departmentDA.GetDepartmentAsync(employee.Department);

            if (dept == null)
                throw new Exception("The Department do not exist");
            if (perm == null)
                throw new Exception("The Permission do not exist");

            //Upload the image to Google Cloud Storage
            var uniqueFileName = Path.GetRandomFileName();
            using var fileStream = file.OpenReadStream();
            var originalImageUrl = await _googleCloudStorageService.UploadFileAsync(fileStream, uniqueFileName, file.ContentType);

            // Step 4: Process and crop the image using Imagga or any similar service
            var croppedImagePath = await _imaggaService.GetFaceDetectionCropImageUrl(originalImageUrl, employee.Name);

            // Step 5: Upload the cropped image to Google Cloud Storage
            var croppedFileName = $"cropped_{uniqueFileName}";
            using var croppedImageStream = new FileStream(croppedImagePath, FileMode.Open, FileAccess.Read);
            var croppedImageUrl = await _googleCloudStorageService.UploadFileAsync(croppedImageStream, croppedFileName, "image/jpeg");


            string query = $@"
                INSERT INTO Employee (employee_id, person_id, position, dept_id, image_url, permission_id)
                VALUES ({personId+30}, {personId}, '{employee.Position}', {employee.Department}, '{croppedImageUrl}', {employee.Permission});
                SELECT SCOPE_IDENTITY();";


            DataTable result = await _databaseService.ExecuteQueryAsync(query);

            if (result.Rows.Count > 0)
            {
                return personId + 30;
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
                    department.Id,
                    row["image_url"].ToString(),
                    permission.Id
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
                int departmentId = Convert.ToInt32(row["dept_id"]);
                int permissionId = Convert.ToInt32(row["permission_id"]);
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
                    department.Id,
                    row["image_url"].ToString(),
                    permission.Id
                ));
            }

            return employees;
        }


        public async Task<int> UpdateEmployeeAsync(Employee employee)
        {
            string query = $@"
                UPDATE Employee 
                SET Name = '{employee.Name}', Age = {employee.Age}, Address = '{employee.Address}', 
                    Position = '{employee.Position}', DepartmentId = {employee.Department}, 
                    ImageUrl = '{employee.ImageUrl}', PermissionId = {employee.Permission}
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
