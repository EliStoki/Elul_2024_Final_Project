using Server.Models.Infrastructure;
using System.Data;

namespace Server.Models.DataAccess.Person;

public class PersonCommand
{
    private readonly DataBaseService _databaseService;

    public PersonCommand()
    {
        _databaseService = DataBaseService.GetInstance();
    }

    // Method to create a new person
    public async Task<int> CreatePersonAsync(Models.Person person)
    {
        string query = $@"
                INSERT INTO Person (Name, Age, Address) 
                VALUES ('{person.Name}', {person.Age}, '{person.Address}');
                SELECT SCOPE_IDENTITY();";

        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
        {
            return Convert.ToInt32(result.Rows[0][0]);
        }

        throw new Exception("Failed to create a new person.");
    }

    // Method to update a person
    public async Task<int> UpdatePersonAsync(Models.Person person)
    {
        string query = $@"
                UPDATE Person 
                SET Name = '{person.Name}', Age = {person.Age}, Address = '{person.Address}' 
                WHERE person_id = {person.Id}";

        return await _databaseService.ExecuteNonQueryAsync(query);
    }

    // Method to delete a person
    public async Task<int> DeletePersonAsync(int id)
    {
        string query = $"DELETE FROM Person WHERE person_id = {id}";
        return await _databaseService.ExecuteNonQueryAsync(query);
    }
}
