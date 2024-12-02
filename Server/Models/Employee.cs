using System.ComponentModel.DataAnnotations;
using Newtonsoft.Json;

namespace Server.Models;

public class Employee : Person
{
    public string Position { get; set; }
    public int Department { get; set; }  // Department object
    public string ImageUrl { get; set; }
    public int Permission { get; set; }  // Permission object

    public Employee()
    {
        
    }

    public Employee(string name, int age, string address, int employeeId, string position, int department, string imageUrl, int permission)
        : base(employeeId, name, age, address)
    {
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


