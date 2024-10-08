using System.Data;
using System.Data.SqlClient;
namespace Server.Models.DA;

public class DatabaseService
{
    private static DatabaseService _instance;
    private static readonly object _lock = new object();
    private readonly string _connectionString;

    // Private constructor to prevent instantiation
    private DatabaseService(IConfiguration configuration)
    {
        _connectionString = configuration.GetConnectionString("SomeeDbConnection");
    }

    // Public method to get the singleton instance
    public static DatabaseService GetInstance(IConfiguration configuration)
    {
        // Ensure thread safety while creating the singleton instance
        if (_instance == null)
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new DatabaseService(configuration);
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
}
