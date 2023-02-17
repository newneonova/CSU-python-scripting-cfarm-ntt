$prismRoot = "D:\LargeFileRepos\2018daycent\DaycentService\JavaVersionDaycentService\BigFilesDontCopy\prismWeather"


function GetFiles($path = $pwd, [string[]]$exclude)
{
    foreach ($item in Get-ChildItem $path)
    {
        if ($exclude | Where {$item -like $_}) { continue }

       
        if (Test-Path $item.FullName -PathType Container)
        {
       
            GetFiles $item.FullName $exclude
        }
        else{
        $item.BaseName.Split(".wth")[0].Split("_") -join ','
       

        }
    }
} 

$allFilesArray = GetFiles $prismRoot



$allFilesArray | Out-File -Append  ./2018existingWeatherFiles.txt



