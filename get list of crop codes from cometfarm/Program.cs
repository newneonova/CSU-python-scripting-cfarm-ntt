// See https://aka.ms/new-console-template for more information
using System.Collections.Concurrent;

Console.WriteLine("Hello, World!");


HashSet<string> processedCodes = new();

foreach(var file in Directory.GetFiles("D:\\CSU Repos\\CSU-python-scripting-cfarm-ntt\\get list of crop codes from cometfarm\\ScheduleFiles", "*.txt", SearchOption.AllDirectories))
{
    ConcurrentBag<string> RawCropCodes = new();
    Parallel.ForEach(File.ReadLines(file), line =>
    {
        if(line.Contains("CROP "))
        {
            var Splitted = line.Split("CROP ", StringSplitOptions.RemoveEmptyEntries);
            for (var i=1;i<Splitted.Length; i++)
            {
                RawCropCodes.Add(Splitted[i].Split()[0].Split("\n")[0].Split("\r")[0].Trim().Replace(",","").Replace(".",""));

            }
        }
    
      
    });
    processedCodes.UnionWith(RawCropCodes);
}

File.WriteAllText("CropCodes.txt", String.Join(System.Environment.NewLine, processedCodes));