// See https://aka.ms/new-console-template for more information
using System.Collections.Concurrent;

Console.WriteLine("Hello, World!");

    
            int Radius = 10;

var LargeFileLocaton = "D:\\LargeFileRepos\\Daycent30Cm\\DaycentService\\DaycentServiceFiles\\BigFilesDontCopy\\100files\\2019spinups_20201117.csv";

  var allLines = new ConcurrentDictionary<string,byte>();
           Parallel.ForEach(File.ReadLines(LargeFileLocaton), s =>
            {
                var asplit = s.Split(',');
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
                         allLines[(y+Y) + "," +(x+X)]=0;
                    }
                }

               
         
            });

var allKnownYXPairs = allLines.Keys;

var allHadFiles = File.ReadAllLines("C:\\Users\\mclay\\Documents\\Github\\CSU-python-scripting-cfarm-ntt\\MissingWeatherFileFromRunningCode\\existingWeatherFiles.txt").ToHashSet();

var inSiteArchiveButNotInFileSystem = allKnownYXPairs.Except(allHadFiles).ToList();
var inFilesButNotInSiteArchive = allHadFiles.Except(allKnownYXPairs);

File.WriteAllLines("inSiteArchiveButmissingFromDirectory.csv", inSiteArchiveButNotInFileSystem);
File.WriteAllLines("inDirectoryButNotInSiteFileArchive.csv", inFilesButNotInSiteArchive);