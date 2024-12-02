
using Server.Models;
using Server.Queries.Permission;
using Server.Models.DataAccess.Permission;

namespace Server.Handlers.QueryHandlers;

public class PermissionQueryHandler
{
    private readonly PermissionQuery _permissionQuery;

    public PermissionQueryHandler(PermissionQuery permissionQuery)
    {
        _permissionQuery = permissionQuery;
    }

    public async Task<Permission> Handle(GetPermissionByIdQuery query)
    {
        return await _permissionQuery.GetPermissionAsync(query.Id);
    }

    public async Task<List<Permission>> Handle(GetAllPermissionsQuery query)
    {
        return await _permissionQuery.GetAllPermissionsAsync();
    }
}

