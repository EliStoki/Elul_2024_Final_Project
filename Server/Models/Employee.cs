using System.ComponentModel.DataAnnotations;

namespace Server.Models;

public class Employee : Person
{
    public string Position { get; set; }
    public Department Department { get; set; }  // Department object
    public string ImageUrl { get; set; }
    public Permission Permission { get; set; }  // Permission object

    public Employee(string name, int age, string address, int employeeId, string position, Department department, string imageUrl, Permission permission)
        : base(employeeId, name, age, address)
    {
        Id = employeeId;
        Position = position;
        Department = department;
        ImageUrl = imageUrl;
        Permission = permission;
    }

    public override string ToString()
    {
        return $"{base.ToString()}, Employee ID: {Id}, Position: {Position}, {Department}, {Permission}";
    }
}
