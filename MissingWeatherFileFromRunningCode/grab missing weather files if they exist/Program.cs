
var ExistingWeatherFilesRootDirectory = "P:\\CFARM\\weather\\prism2019";
var localWeatherFileDumpDirectory = "C:\\Users\\mclay\\Documents\\Github\\CSU-python-scripting-cfarm-ntt\\MissingWeatherFileFromRunningCode\\grab missing weather files if they exist\\prism2019_missing";
var fileHoldingListOfYXToFind = "C:\\Users\\mclay\\Documents\\Github\\CSU-python-scripting-cfarm-ntt\\MissingWeatherFileFromRunningCode\\inSiteArchiveButmissingFromDirectory.csv";

var MissingPairs = File.ReadAllLines(fileHoldingListOfYXToFind);

int count=0;
int missing=0;
Parallel.ForEach(MissingPairs, pair =>
{
    var split = pair.Split(',');
    var LocalFileName = "prism_" + split[0] + "\\" + split[0] + "_" + split[1] + ".wth_1975_2044.wth.bz2";
    var destFileName =  "prism_" + split[0] + "\\" + split[0] + "_" + split[1] + ".wth_1975_2044.wth_updated2019.wth.bz2";
    var origin = Path.Combine(ExistingWeatherFilesRootDirectory, LocalFileName);
    var destinationDir = Path.Combine(localWeatherFileDumpDirectory,  "prism_" + split[0]);
        var destination = Path.Combine(localWeatherFileDumpDirectory,  destFileName);
 
    if (File.Exists(origin))
    {
        Directory.CreateDirectory(destinationDir);
        File.Copy(origin, destination);
        Interlocked.Increment(ref count);

    }
    else
    {
             Interlocked.Increment(ref missing);
    }


});

Console.WriteLine("transfered " + count + " files.  Missing "+missing+" files.");