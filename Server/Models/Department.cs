using System.ComponentModel.DataAnnotations;

namespace Server.Models;

public class Department
{
    [Key]
    public int Id { get; set; }
    public string DeptName { get; set; }

    public Department(int deptId, string deptName)
    {
        Id = deptId;
        DeptName = deptName;
    }

    public override string ToString()
    {
        return $"Department: {DeptName}, ID: {Id}";
    }
}
