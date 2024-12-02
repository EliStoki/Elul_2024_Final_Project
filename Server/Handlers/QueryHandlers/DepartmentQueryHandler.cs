using Server.Models.DA;
using Server.Models;
using Server.Queries.Department;
using Server.Models.DataAccess.Department;

namespace Server.Handlers.QueryHandlers;

public class DepartmentQueryHandler
{
    private readonly DepartmentQuery _departmentQuery;

    public DepartmentQueryHandler(DepartmentQuery departmentQuery)
    {
        _departmentQuery = departmentQuery;
    }

    public async Task<Department> Handle(GetDepartmentByIdQuery query)
    {
        return await _departmentQuery.GetDepartmentAsync(query.Id);
    }

    public async Task<List<Department>> Handle(GetAllDepartmentsQuery query)
    {
        return await _departmentQuery.GetAllDepartmentsAsync();
    }
}

