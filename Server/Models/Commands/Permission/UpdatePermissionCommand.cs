namespace Server.Models.Commands.Permission
{
    public class UpdatePermissionCommand
    {
        public int Id { get; set; }
        public int FloorLevel { get; set; }
        public string Building { get; set; }
    }

}
