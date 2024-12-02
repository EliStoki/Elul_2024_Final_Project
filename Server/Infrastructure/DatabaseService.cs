using System.Data;
using System.Data.SqlClient;
namespace Server.Infrastructure;

public class DataBaseService
{
    private static DataBaseService _instance;
    private static readonly object _lock = new object();
    private readonly string _connectionString;

    // Private constructor to prevent instantiation
    private DataBaseService()
    {
        try
        {
            _connectionString = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json")
                .Build().GetConnectionString("SomeeDbConnection");

        }
        catch (Exception ex)
        {
            // Handle exceptions as necessary
            Console.WriteLine($"An error occurred while setting the connection string: {ex.Message}");
            throw; // Optionally rethrow the exception if you want to handle it further up the call stack
        }
    }
    // Public method to get the singleton instance
    public static DataBaseService GetInstance()
    {
        // Ensure thread safety while creating the singleton instance
        if (_instance == null)
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new DataBaseService();
                }
            }
        }
        return _instance;
    }

    // Example method to execute a SQL query and return data
    public async Task<DataTable> ExecuteQueryAsync(string query)
    {
        DataTable dataTable = new DataTable();
        try
        {
            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    SqlDataAdapter adapter = new SqlDataAdapter(command);
                    adapter.Fill(dataTable);
                }
            }
        }
        catch (Exception ex)
        {
            // Handle exceptions as necessary
            Console.WriteLine($"An error occurred: {ex.Message}");
        }

        return dataTable;
    }

    public async Task<int> ExecuteNonQueryAsync(string query)
    {
        int affectedRows = 0;

        try
        {
            using (SqlConnection connection = new SqlConnection(_connectionString))
            {
                await connection.OpenAsync();

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    affectedRows = await command.ExecuteNonQueryAsync();
                }
            }
        }
        catch (Exception ex)
        {
            // Handle exceptions as necessary
            Console.WriteLine($"An error occurred: {ex.Message}");
        }

        return affectedRows;
    }

}
