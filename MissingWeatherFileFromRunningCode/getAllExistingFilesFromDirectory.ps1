$prismRoot = "D:\LargeFileRepos\Daycent30Cm\DaycentService\DaycentServiceFiles\BigFilesDontCopy\prism2019"


function GetFiles($path = $pwd, [string[]]$exclude)
{
$count=0
    foreach ($item in Get-ChildItem $path)
    {
        if ($exclude | Where {$item -like $_}) { continue }

       
        if (Test-Path $item.FullName -PathType Container)
        {
       
            GetFiles $item.FullName $exclude
        }
        else{
        $item.BaseName.Split(".wth")[0].Split("_") -join ','
        $count++
        if($count -eq 100){
         write-host  $item.BaseName
         $count=0
        }
      

        }
    }
} 

$allFilesArray = GetFiles $prismRoot



$allFilesArray | Out-File -Append  ./existingWeatherFiles.txt



