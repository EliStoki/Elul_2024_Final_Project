using Server.Models;
using Server.Models.Commands.Permission;
using Server.Models.DataAccess.Permission;

namespace Server.Handlers.CommandHandlers;

public class PermissionCommandHandler
{
    private readonly PermissionCommand _permissionCommand;

    public PermissionCommandHandler(PermissionCommand permissionCommand)
    {
        _permissionCommand = permissionCommand;
    }

    public async Task<int> Handle(CreatePermissionCommand command)
    {
        var permission = new Permission(0, command.FloorLevel, command.Building);
        return await _permissionCommand.CreatePermissionAsync(permission);
    }

    public async Task<int> Handle(UpdatePermissionCommand command)
    {
        var permission = new Permission(command.Id, command.FloorLevel, command.Building);
        return await _permissionCommand.UpdatePermissionAsync(permission);
    }

    public async Task<int> Handle(DeletePermissionCommand command)
    {
        return await _permissionCommand.DeletePermissionAsync(command.Id);
    }
}

