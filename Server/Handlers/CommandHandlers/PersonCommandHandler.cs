using Server.Models.DataAccess.Person;
using Server.Models;
using Server.Commands.Person;

namespace Server.Handlers.CommandHandlers;

public class PersonCommandHandler
{
    private readonly PersonCommand _personCommand;

    public PersonCommandHandler(PersonCommand personCommand)
    {
        _personCommand = personCommand;
    }

    public async Task<int> Handle(CreatePersonCommand command)
    {
        var person = new Person(0, command.Name, command.Age, command.Address);
        return await _personCommand.CreatePersonAsync(person);
    }

    public async Task<int> Handle(UpdatePersonCommand command)
    {
        var person = new Person(command.Id, command.Name, command.Age, command.Address);
        return await _personCommand.UpdatePersonAsync(person);
    }

    public async Task<int> Handle(DeletePersonCommand command)
    {
        return await _personCommand.DeletePersonAsync(command.Id);
    }
}
