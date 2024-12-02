using Server.Models.DataAccess.Person;
using Server.Models;
using Server.Models.Queries.Person;

namespace Server.Handlers.QueryHandlers;

public class PersonQueryHandler
{
    private readonly PersonQuery _personQuery;

    public PersonQueryHandler(PersonQuery personQuery)
    {
        _personQuery = personQuery;
    }

    public async Task<Person> Handle(GetPersonByIdQuery query)
    {
        return await _personQuery.GetPersonAsync(query.Id);
    }

    public async Task<List<Person>> Handle(GetAllPersonsQuery query)
    {
        return await _personQuery.GetAllPersonsAsync();
    }
}

