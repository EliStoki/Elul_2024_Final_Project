namespace Server.Models;

public class Department
{
    public int DeptId { get; set; }
    public string DeptName { get; set; }

    public Department(int deptId, string deptName)
    {
        DeptId = deptId;
        DeptName = deptName;
    }

    public override string ToString()
    {
        return $"Department: {DeptName}, ID: {DeptId}";
    }
}
