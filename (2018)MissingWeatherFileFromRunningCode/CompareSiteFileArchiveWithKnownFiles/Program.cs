// See https://aka.ms/new-console-template for more information
using System.Collections.Concurrent;
using System.ComponentModel.DataAnnotations;
using System.Xml.XPath;

Console.WriteLine("Hello, World!");

    
            int Radius = 10;

var LargeFileLocaton = "D:\\LargeFileRepos\\2018daycent\\DaycentService\\JavaVersionDaycentService\\BigFilesDontCopy\\eqruns2017_spinup_20200205.csv";


var allCodes = new ConcurrentBag<(string,string)>();




//OK 700,000 lines, maybe do an ind

//OK this is very big and very slow so going to do it in bits
           Parallel.ForEach( File.ReadAllLines(LargeFileLocaton), (s,stat,idex) =>
            {
                   var asplit = s.Split(',');
                allCodes.Add((asplit[3], asplit[4]));
         
            });
var allCodesHash = allCodes.ToHashSet();
var allCodeInt = allCodesHash.Select(pair =>
{
    int x = 0;
    int y = 0;
    int.TryParse(pair.Item1, out x);
    int.TryParse(pair.Item2, out y);
    return (x, y);
}).ToList();


var allAllALLLCODES = new ConcurrentDictionary<string, byte>();
Parallel.ForEach(allCodeInt, pair =>
{
    var x= pair.Item1;
    var y= pair.Item2;
    int lower = -Radius;
                int upper = Radius;
                for(var X=lower; X <= upper; X++)
                {
                    for(var Y=lower; Y<=upper; Y++)
                    {
                         allAllALLLCODES[(y+Y) + "," +(x+X)]=0;
                    }
                }

                

});



var allKnownYXPairs= allAllALLLCODES.Keys;

var allHadFiles = File.ReadAllLines("C:\\Users\\mclay\\Documents\\Github\\CSU-python-scripting-cfarm-ntt\\(2018)MissingWeatherFileFromRunningCode\\2018existingWeatherFiles.txt").ToHashSet();

var inSiteArchiveButNotInFileSystem = allKnownYXPairs.Except(allHadFiles).ToList();
var inFilesButNotInSiteArchive = allHadFiles.Except(allKnownYXPairs);

File.WriteAllLines("2018inSiteArchiveButmissingFromDirectory.csv", inSiteArchiveButNotInFileSystem);
File.WriteAllLines("2018inDirectoryButNotInSiteFileArchive.csv", inFilesButNotInSiteArchive);