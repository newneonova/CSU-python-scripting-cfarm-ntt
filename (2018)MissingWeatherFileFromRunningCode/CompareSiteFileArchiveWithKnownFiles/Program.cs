// See https://aka.ms/new-console-template for more information
using System.Collections.Concurrent;
using System.ComponentModel.DataAnnotations;

Console.WriteLine("Hello, World!");

    
            int Radius = 10;

var LargeFileLocaton = "D:\\LargeFileRepos\\2018daycent\\DaycentService\\JavaVersionDaycentService\\BigFilesDontCopy\\eqruns2017_spinup_20200205.csv";


var AllBags = new ConcurrentBag<HashSet<string>>(); 

var AllLines = File.ReadAllLinesAsync(LargeFileLocaton).Result.Chunk(10000);


//OK 700,000 lines, maybe do an ind
           Parallel.ForEach(AllLines, (s,stat,idex) =>
            {
                var bigList = new List<string>();
                foreach(var line in s)
                {
                      var asplit = line.Split(',');
                int x = 0;
                int y = 0;
                int.TryParse(asplit[3], out x);
                int.TryParse(asplit[4],out y);
                int lower = -Radius;
                int upper = Radius;
                for(var X=lower; X <= upper; X++)
                {
                    for(var Y=lower; Y<=upper; Y++)
                    {
                         bigList.Add((y+Y) + "," +(x+X));
                    }
                }

                }
                AllBags.Add(bigList.ToHashSet());
               

               
         
            });

var allKnownYXPairsList  = new List<string>();
foreach(var bag in AllBags)
{
    allKnownYXPairsList.AddRange(bag.ToList());
}
var allKnownYXPairs= allKnownYXPairsList.ToHashSet();

var allHadFiles = File.ReadAllLines("\"C:\\Users\\mclay\\Documents\\Github\\CSU-python-scripting-cfarm-ntt\\(2018)MissingWeatherFileFromRunningCode\\2018existingWeatherFiles.txt\"t").ToHashSet();

var inSiteArchiveButNotInFileSystem = allKnownYXPairs.Except(allHadFiles).ToList();
var inFilesButNotInSiteArchive = allHadFiles.Except(allKnownYXPairs);

File.WriteAllLines("2018inSiteArchiveButmissingFromDirectory.csv", inSiteArchiveButNotInFileSystem);
File.WriteAllLines("2018inDirectoryButNotInSiteFileArchive.csv", inFilesButNotInSiteArchive);