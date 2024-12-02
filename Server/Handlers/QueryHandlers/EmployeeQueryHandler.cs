
using Server.Models;
using Server.Models.DataAccess.Employee;
using Server.Models.Queries.Employee;

namespace Server.Handlers.QueryHandlers;

public class EmployeeQueryHandler
{
    private readonly EmployeeQuery _employeeQuery;

    public EmployeeQueryHandler(EmployeeQuery employeeQuery)
    {
        _employeeQuery = employeeQuery;
    }

    public async Task<Employee> Handle(GetEmployeeByIdQuery query)
    {
        return await _employeeQuery.GetEmployeeAsync(query.Id);
    }

    public async Task<List<Employee>> Handle(GetAllEmployeesQuery query)
    {
        return await _employeeQuery.GetAllEmployeesAsync();
    }
}

