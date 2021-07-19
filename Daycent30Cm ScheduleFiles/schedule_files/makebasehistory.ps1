$eqruns = "C:\Users\RSF\Desktop\schedule_files\schedule_files\base_history\"

$out =  "C:\Users\RSF\Desktop\schedule_files\schedule_files\baseHistoryLineMake"
if (Test-Path $out) 
{
  Remove-Item $out
}
$frontEndOfLine = "INSERT INTO cfarm.base_history_lookup_20210714 (mlra, hydric, irrig, grazetill, id_history, filename, sch) VALUES ("

Get-ChildItem $eqruns -Filter *.sch |
Foreach-Object{
$content = Get-Content $_.FullName
$name = $_.BaseName
$array = $name.Split("_")
Write-Host $array[1]
$line = "$frontEndOfLine '$($array[1])','$($array[2])','$($array[3])','$($array[4])','$($name)','$content');"
Add-Content -Path $out -Value $line
}


