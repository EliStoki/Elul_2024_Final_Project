using Server.Commands.Department;
using Server.Models;
using Server.Models.DataAccess.Department;

namespace Server.Handlers.CommandHandlers;

public class DepartmentCommandHandler
{
    private readonly DepartmentCommand _departmentCommand;

    public DepartmentCommandHandler(DepartmentCommand departmentCommand)
    {
        _departmentCommand = departmentCommand;
    }

    public async Task<int> Handle(CreateDepartmentCommand command)
    {
        var department = new Department
        {
            DeptName = command.DeptName
        };

        return await _departmentCommand.CreateDepartmentAsync(department);
    }

    public async Task<int> Handle(UpdateDepartmentCommand command)
    {
        var department = new Department
        {
            Id = command.Id,
            DeptName = command.DeptName
        };

        return await _departmentCommand.UpdateDepartmentAsync(department);
    }

    public async Task<int> Handle(DeleteDepartmentCommand command)
    {
        return await _departmentCommand.DeleteDepartmentAsync(command.Id);
    }
}
