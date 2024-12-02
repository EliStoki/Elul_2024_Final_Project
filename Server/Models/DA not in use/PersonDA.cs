using Microsoft.AspNetCore.Http.HttpResults;
using Server.Infrastructure;
using System.Data;

namespace Server.Models.DA;

public class PersonDA
{
    private DataBaseService _databaseService = DataBaseService.GetInstance();

    public PersonDA()
    { }

    public async Task<int> CreatePersonAsync(Person person)
    {
        string query = $"INSERT INTO Person (Name, Age, Address) VALUES ('{person.Name}', {person.Age}, '{person.Address}'); " +
                       "SELECT SCOPE_IDENTITY();";

        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        // Check if the query returned the new ID (should return a scalar result with the new ID)
        if (result.Rows.Count > 0 && result.Rows[0][0] != DBNull.Value)
        {
            int newPersonId = Convert.ToInt32(result.Rows[0][0]);
            return newPersonId;
        }

        return -1; // or throw an exception to indicate failure
    }


    public async Task<Person> GetPersonAsync(int id)
    {
        string query = $"SELECT * FROM Person WHERE person_id = {id}";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);
        if (result.Rows.Count > 0)
        {
            DataRow row = result.Rows[0];
            Person person = new Person(
                Convert.ToInt32(row[0]),
                row["Name"].ToString(),
                Convert.ToInt32(row["Age"]),
                row["Address"].ToString()
            );
            return person;
        }
        return null;
    }

    public async Task<List<Person>> GetAllPersonsAsync()
    {
        string query = "SELECT * FROM Person";
        DataTable result = await _databaseService.ExecuteQueryAsync(query);

        List<Person> persons = new List<Person>();

        foreach (DataRow row in result.Rows)
        {
            Person person = new Person(
                Convert.ToInt32(row[0]),
                row["Name"].ToString(),
                Convert.ToInt32(row["Age"]),
                row["Address"].ToString()
            );
            persons.Add(person);
        }

        return persons;
    }

    public async Task<int> UpdatePersonAsync(Person person)
    {
        string query = $"UPDATE Person SET Name = '{person.Name}', Age = {person.Age}, Address = '{person.Address}' WHERE person_Id = {person.Id}";
        int affectedRows = await _databaseService.ExecuteNonQueryAsync(query);
        return affectedRows;
    }

    public async Task<int> DeletePersonAsync(int id)
    {
        string query = $"DELETE FROM Person WHERE person_Id = {id}";
        int affectedRows = await _databaseService.ExecuteNonQueryAsync(query);
        return affectedRows;
    }

}
