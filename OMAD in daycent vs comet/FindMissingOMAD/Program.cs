// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");


double value = 1;
var mainString = File.ReadAllText("omad.100");
List<string> missingManure = new();
double adder = .1;
while (value < 40)
{
    var checker = "A" + value.ToString("0.#");
    if (!mainString.Contains(checker))
    {
        missingManure.Add(checker);
    }
    if (value >= 25)
    {
        adder = 1;
    }
    value += adder;
   


}
File.WriteAllLines("MissingMan.txt", missingManure);