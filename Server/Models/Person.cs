namespace Server.Models
{
    public class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public string Address { get; set; }

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

}
