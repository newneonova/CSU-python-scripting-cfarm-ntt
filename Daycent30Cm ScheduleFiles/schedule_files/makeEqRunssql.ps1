$eqruns = "C:\Users\RSF\Desktop\schedule_files\schedule_files\equil\"

$out =  "C:\Users\RSF\Desktop\schedule_files\schedule_files\eqRunTableMake"
if (Test-Path $out) 
{
  Remove-Item $out
}
$frontEndOfLine = "INSERT INTO cfarm.daycent_30cm_equil_schedule_files (mlra, hydric, file) VALUES ("

Get-ChildItem $eqruns -Filter *.sch |
Foreach-Object{
$content = Get-Content $_.FullName
$name = $_.BaseName
$array = $name.Split("_")
Write-Host $array[1]
$line = "$frontEndOfLine '$($array[1])','$($array[2])','$content');"
Add-Content -Path $out -Value $line
}


