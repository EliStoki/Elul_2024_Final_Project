namespace Server.Models.Commands.Person
{
    public class CreatePersonCommand
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public string Address { get; set; }
    }
}
