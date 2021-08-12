$eqruns = ".\spinup\"

$out =  "spinuplinemake"
if (Test-Path $out) 
{
  Remove-Item $out
}
$frontEndOfLine = "INSERT INTO cfarm.daycent_30cm_spinup_schedule_files (mlra, hydric, irrig, grazetill, id_history, filename, sch) VALUES ("

$collection = New-Object Collections.Generic.List[String]
Get-ChildItem $eqruns -Filter *.sch |
Foreach-Object{
$content = Get-Content -Path $_.FullName -Raw
$name = $_.BaseName
$array = $name.Split("_")
Write-Host $array[1] $array[5]
$line = "$frontEndOfLine '$($array[1])','$($array[2])','$($array[3])','$($array[4])','$($array[5])','$($name)','$content');"
$collection.Add($line)
}
Add-Content -Path $out -Value $collection

