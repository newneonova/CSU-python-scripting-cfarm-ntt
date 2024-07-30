// See https://aka.ms/new-console-template for more information
using System.Reflection;

Console.WriteLine("Hello, World!");

var baseDir = Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.Parent.FullName;
var knownCrops = File.ReadAllLines(baseDir+@"\cropCodes.txt");
var crop100 = File.ReadAllText(baseDir+@"\crop.100");


List<string> missingCrops = new();
foreach (var crop in knownCrops)
{

    if (!crop100.Contains(crop))
    {
        missingCrops.Add(crop);
    }

}
File.WriteAllLines("missingCrops.txt", missingCrops);