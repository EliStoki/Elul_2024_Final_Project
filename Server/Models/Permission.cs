namespace Server.Models
{
    public class Permission
    {
        public int FloorLevel { get; set; }
        public string Building { get; set; }

        public Permission(int floorLevel, string building)
        {
            FloorLevel = floorLevel;
            Building = building;
        }

        public override string ToString()
        {
            return $"Levels: {FloorLevel}, Buildings: {Building}";
        }
    }

}
