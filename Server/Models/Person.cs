using System.ComponentModel.DataAnnotations;

namespace Server.Models;

public class Person
{

    [Key]
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }
    public string Address { get; set; }

    public Person()
    {

    }
    public Person(int id, string name, int age, string address)
    {
        Id = id;
        Name = name;
        Age = age;
        Address = address;
    }

    public Person(string name, int age, string address)
    {
        Name = name;
        Age = age;
        Address = address;
    }

    public override string ToString()
    {
        return $"Name: {Name}, Age: {Age}, Address: {Address}";
    }
}
