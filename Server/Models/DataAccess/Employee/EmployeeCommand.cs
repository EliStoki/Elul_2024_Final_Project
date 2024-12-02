using Server.Infrastructure;
using Server.Models.DA;
using Server.Models.DataAccess.Department;
using Server.Models.DataAccess.Permission;
using Server.Models.DataAccess.Person;
using Server.Services;
using System.Data;

namespace Server.Models.DataAccess.Employee;

public class EmployeeCommand
{
    private readonly DataBaseService _databaseService;
    private readonly GoogleCloudStorageService _googleCloudStorageService;
    private readonly ImaggaService _imaggaService;
    private readonly DepartmentQuery _departmentQuery;
    private readonly PermissionQuery _permissionQuery;
    private readonly PersonCommand _personCommand;

    public EmployeeCommand()
    {
        _databaseService = DataBaseService.GetInstance();
        _googleCloudStorageService = new GoogleCloudStorageService();
        _imaggaService = new ImaggaService();
        _departmentQuery = new DepartmentQuery();
        _permissionQuery = new PermissionQuery();
        _personCommand = new PersonCommand();
    }

    // Method to create a new employee
    public async Task<int> CreateEmployeeAsync(Models.Employee employee, IFormFile file)
    {
        Models.Person person = new(employee.Name, employee.Age, employee.Address);
        var personId = await _personCommand.CreatePersonAsync(person);

        var dept = await _departmentQuery.GetDepartmentAsync(employee.Department);
        var perm = await _permissionQuery.GetPermissionAsync(employee.Permission);

        if (dept == null)
            throw new Exception("The Department does not exist");
        if (perm == null)
            throw new Exception("The Permission does not exist");

        // Upload original image
        var uniqueFileName = Path.GetRandomFileName();
        using var fileStream = file.OpenReadStream();
        var originalImageUrl = await _googleCloudStorageService.UploadFileAsync(fileStream, uniqueFileName, file.ContentType);

        // Process and crop the image using Imagga
        var croppedImagePath = await _imaggaService.GetFaceDetectionCropImageUrl(originalImageUrl, employee.Name);

        // Upload the cropped image
        var croppedFileName = $"cropped_{uniqueFileName}";
        using var croppedImageStream = new FileStream(croppedImagePath, FileMode.Open, FileAccess.Read);
        var croppedImageUrl = await _googleCloudStorageService.UploadFileAsync(croppedImageStream, croppedFileName, "image/jpeg");

        // Insert into Employee table
        string query = $@"
                INSERT INTO Employee (employee_id, person_id, position, dept_id, image_url, permission_id)
                VALUES ({personId + 30}, {personId}, '{employee.Position}', {employee.Department}, '{croppedImageUrl}', {employee.Permission});
                SELECT SCOPE_IDENTITY();";

        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0)
        {
            return personId + 30;
        }

        return -1;
    }

    // Method to update an employee
    public async Task<int> UpdateEmployeeAsync(Models.Employee employee)
    {
        string query = $@"
                UPDATE Employee 
                SET position = '{employee.Position}', dept_id = {employee.Department}, 
                    image_url = '{employee.ImageUrl}', permission_id = {employee.Permission}
                WHERE employee_id = {employee.Id}";

        return await _databaseService.ExecuteNonQueryAsync(query);
    }

    // Method to delete an employee
    public async Task<int> DeleteEmployeeAsync(int id)
    {
        string query = $"DELETE FROM Employee WHERE employee_id = {id}";
        return await _databaseService.ExecuteNonQueryAsync(query);
    }
}
