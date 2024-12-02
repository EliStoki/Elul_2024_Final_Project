using Server.Infrastructure;
using System.Data;

namespace Server.Models.DataAccess.Person;

public class PersonQuery
{
    private readonly DataBaseService _databaseService;

    public PersonQuery()
    {
        _databaseService = DataBaseService.GetInstance();
    }

    // Method to get a person by ID
    public async Task<Models.Person> GetPersonAsync(int id)
    {
        string query = $"SELECT * FROM Person WHERE person_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            return new Models.Person(
                Convert.ToInt32(row["person_id"]),
                row["Name"].ToString(),
                Convert.ToInt32(row["Age"]),
                row["Address"].ToString()
            );
        }

        return null;
    }

    // Method to get all persons
    public async Task<List<Models.Person>> GetAllPersonsAsync()
    {
        string query = "SELECT * FROM Person";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        var persons = new List<Models.Person>();
        foreach (DataRow row in result.Rows)
        {
            persons.Add(new Models.Person(
                Convert.ToInt32(row["person_id"]),
                row["Name"].ToString(),
                Convert.ToInt32(row["Age"]),
                row["Address"].ToString()
            ));
        }

        return persons;
    }
}
