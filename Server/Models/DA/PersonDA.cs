namespace Server.Models.DA;

public class PersonDA
{
    private DatabaseService _databaseService = new();

    public PersonDA()
    {
        _databaseService = databaseService;
    }
}
