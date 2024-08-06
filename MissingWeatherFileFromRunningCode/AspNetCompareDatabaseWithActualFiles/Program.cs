//HAve previously done the work in powershell, want to try again with a more famillar language to compare.



//first need to build a set of all known weather files
//the weather files are located in D:\LargeFileRepos\Daycent30Cm\DaycentService\DaycentServiceFiles\BigFilesDontCopy\prism2019,  we just want (gridy,gridx) 
using System.Text;

string actualWeatherFileRootDirectory = "D:\\LargeFileRepos\\Daycent30Cm\\DaycentService\\DaycentServiceFiles\\BigFilesDontCopy\\prism2019";

Dictionary<(string, string),bool> ActualWeatherFileCollectionDictionary = new();
var hadFiles = Directory.GetFiles(actualWeatherFileRootDirectory, "*.bz2", SearchOption.AllDirectories).Select(x=>Path.GetFileName(x));
foreach (var file in hadFiles)
{
    var yx=file.Split(".wth")[0].Split('_');
    ActualWeatherFileCollectionDictionary[(yx[0], yx[1])] = true;
}
var ActualWeatherFileCollection = ActualWeatherFileCollectionDictionary.Keys.ToHashSet();

Dictionary<(string, string),bool> DatabaseTableCollectionDictionary  = new();

//the existing database table is at "C:\Users\mclay\Csu specific repository\CSU-python-scripting-cfarm-ntt\MissingWeatherFileFromRunningCode\FullGoogleMercatorTableReturn.csv"
var tableDump = @"C:\Users\mclay\Csu specific repository\CSU-python-scripting-cfarm-ntt\MissingWeatherFileFromRunningCode\FullGoogleMercatorTableReturn.csv";
var alreadyremoved = false;
foreach(var line in File.ReadAllLines(tableDump))
{
    var yx = line.Split(',');
    if (!alreadyremoved && yx[0].Contains("gridy"))
    {
        alreadyremoved = true;
         
    }
    else
    {
          DatabaseTableCollectionDictionary[(yx[0], yx[1])] = true;
    }
 


}
var   DatabaseTableCollection = DatabaseTableCollectionDictionary.Keys.ToHashSet();


var FilesExistButNoEntryInTable = ActualWeatherFileCollection.Except(DatabaseTableCollection).ToList().Select(x=>x.Item1+","+x.Item2);
File.WriteAllLines("FilesExistButNoEntryInTable.txt", FilesExistButNoEntryInTable);
var EntryExistButNoFiles = DatabaseTableCollection.Except(ActualWeatherFileCollection).ToList().Select(x=>x.Item1+","+x.Item2);
File.WriteAllLines("EntryExistButNoFiles.txt", EntryExistButNoFiles);
var FileInTableAndInCollection = DatabaseTableCollection.Intersect(ActualWeatherFileCollection).ToList().Select(x=>x.Item1+","+x.Item2);
File.WriteAllLines("FileInTableAndInCollection.txt", FileInTableAndInCollection);


//update  public.prism_centroids_google_mercator set have_weather_file = FALSE where (gridy,gridx) in (

var lines = new List<string>();

var count = 1;
var sb = new StringBuilder();
sb.Append("update  public.prism_centroids_google_mercator set have_weather_file = FALSE where (gridy,gridx) in (");
var inList = new List<string>();
foreach(var exclude in EntryExistButNoFiles)
{
   // lines.Add($"update  public.prism_centroids_google_mercator set have_weather_file = FALSE where (gridy,gridx) = {exclude}");
    if(count%500 == 0)
    {
        sb.Append($"{String.Join(',',inList)});");
        lines.Add(sb.ToString());
        sb = new();
        sb.Append("update  public.prism_centroids_google_mercator set have_weather_file = FALSE where (gridy,gridx) in (");
        inList = new();

    }
    inList.Add($"({exclude})");
    count++;

}
  sb.Append($"{String.Join(',',inList)});");
        lines.Add(sb.ToString());

File.WriteAllLines("SqlToMakeTableAware.sql", lines);