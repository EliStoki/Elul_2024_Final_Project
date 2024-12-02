using Server.Commands.Employee;
using Server.Models.DA;
using Server.Models;
using Server.Models.DataAccess.Employee;

namespace Server.Handlers.CommandHandlers;

public class EmployeeCommandHandler
{

    private readonly EmployeeCommand _employeeCommand;

    public EmployeeCommandHandler(EmployeeCommand employeeCommand)
    {
        _employeeCommand = employeeCommand;
    }

    public async Task<int> Handle(CreateEmployeeCommand command, IFormFile file)
    {
        var employee = new Employee
        {
            Name = command.Name,
            Age = command.Age,
            Address = command.Address,
            Position = command.Position,
            Department = command.Department,
            ImageUrl = command.ImageUrl,
            Permission = command.Permission
        };

        return await _employeeCommand.CreateEmployeeAsync(employee, file);
    }

    public async Task<int> Handle(UpdateEmployeeCommand command)
    {
        var employee = new Employee
        {
            Id = command.Id,
            Name = command.Name,
            Age = command.Age,
            Address = command.Address,
            Position = command.Position,
            Department = command.Department,
            ImageUrl = command.ImageUrl,
            Permission = command.Permission
        };

        return await _employeeCommand.UpdateEmployeeAsync(employee);
    }

    public async Task<int> Handle(DeleteEmployeeCommand command)
    {
        return await _employeeCommand.DeleteEmployeeAsync(command.Id);
    }
}
