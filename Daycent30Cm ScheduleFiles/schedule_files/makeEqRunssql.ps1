$eqruns = ".\equil\"

$out =  "eqRunTableMake"
if (Test-Path $out) 
{
  Remove-Item $out
}
$frontEndOfLine = "INSERT INTO cfarm.daycent_30cm_equil_schedule_files (mlra, hydric, sch) VALUES ("

$collection = New-Object Collections.Generic.List[String]
Get-ChildItem $eqruns -Filter *.sch |
Foreach-Object{
$content = Get-Content -Path $_.FullName -Raw
$name = $_.BaseName
$array = $name.Split("_")
Write-Host $array[1]
$line = "$frontEndOfLine '$($array[1])','$($array[2])','$content');"
$collection.Add($line)
}
Add-Content -Path $out -Value $collection


