$AllDatabase = ".\FullGoogleMercatorTableReturn.csv"
$AllFiles = ".\existingWeatherFiles.txt"

#parse allFiles to a hashSet, 
$allFileHash = [System.Collections.Generic.HashSet[String]] @(Get-Content $AllFiles)
$AllDatabaseTable = @{}
foreach($row in Get-Content $AllDatabase){
$key = $row.Split(',')
$AllDatabaseTable[$($key[0],$key[1] -join ',')] = $row
}

foreach($item in $allFileHash){
$AllDatabaseTable.Remove($item)
}

$AllDatabaseTable.Values | Out-File -Append  ./inDbButMissingFile.txt