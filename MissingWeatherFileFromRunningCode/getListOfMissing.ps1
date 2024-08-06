$AllDatabase = ".\FullGoogleMercatorTableReturn.csv"
$AllFiles = ".\existingWeatherFiles.txt"

#parse allFiles to a hashSet, 
$allFileHash = [System.Collections.Generic.HashSet[String]] @(Get-Content $AllFiles)
$AllDatabaseTable = @{}
foreach($row in Get-Content $AllDatabase){
$key = $row.Split(',')
$AllDatabaseTable[$($key[0],$key[1] -join ',')] = "("+$($key[0],$key[1] -join ',')+")"
}

foreach($item in $allFileHash){
$AllDatabaseTable.Remove($item)
}
$lister = $AllDatabaseTable.Values| Sort-Object

$finalLines = New-Object System.Collections.Generic.List[System.String]

$count = 1
$FinString="update  public.prism_centroids_google_mercator set have_weather_file = FALSE where (gridy,gridx) in ("
foreach($row in $lister){
	if($count % 500 -eq 0){
		$FinString+=");"
		$finalLines.Add($FinString)
		$FinString="update  public.prism_centroids_google_mercator set have_weather_file = FALSE where (gridy,gridx) in ("
	}
	else{
		$FinString+=","
	}
	$FinString+=$row
	
	$count++
	
}
$FinString+=");"
	$finalLines.Add($FinString)


$finalLines | Out-File  ./inDbButMissingFile.txt