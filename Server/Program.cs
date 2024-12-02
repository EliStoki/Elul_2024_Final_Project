
using Server.Handlers.CommandHandlers;
using Server.Handlers.QueryHandlers;
using Server.Models.DA;
using Server.Models.DataAccess.Department;
using Server.Models.DataAccess.Employee;
using Server.Models.DataAccess.Permission;
using Server.Models.DataAccess.Person;

namespace Server
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container
            builder.Services.AddControllers();

            builder.Services.AddScoped<PersonCommandHandler>();
            builder.Services.AddScoped<PersonQueryHandler>();

            // Register Command and Query Handlers
            builder.Services.AddScoped<EmployeeCommandHandler>();
            builder.Services.AddScoped<EmployeeQueryHandler>();

            builder.Services.AddScoped<DepartmentCommandHandler>();
            builder.Services.AddScoped<DepartmentQueryHandler>();

            builder.Services.AddScoped<PermissionCommandHandler>();
            builder.Services.AddScoped<PermissionQueryHandler>();


            // Register DA Classes
            builder.Services.AddScoped<PersonQuery>();
            builder.Services.AddScoped<PersonCommand>();

            builder.Services.AddScoped<EmployeeQuery>();
            builder.Services.AddScoped<EmployeeCommand>();

            builder.Services.AddScoped<PermissionQuery>();
            builder.Services.AddScoped<PermissionCommand>();

            builder.Services.AddScoped<DepartmentQuery>();
            builder.Services.AddScoped<DepartmentCommand>();

            // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            app.UseAuthorization();


            app.MapControllers();

            app.Run();
        }
    }
}
