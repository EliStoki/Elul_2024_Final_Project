namespace Server.Models.Commands.Employee;

public class UpdateEmployeeCommand
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
    public string Address { get; set; }
    public string Position { get; set; }
    public int Department { get; set; }
    public string ImageUrl { get; set; }
    public int Permission { get; set; }
}
