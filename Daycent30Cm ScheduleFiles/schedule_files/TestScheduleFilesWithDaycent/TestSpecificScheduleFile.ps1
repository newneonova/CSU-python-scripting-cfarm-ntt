

cd ..
$RunDirectory = ".\StrippedDownDaycentTestDirectory"
cd $RunDirectory


$copyOut = ".\spinup.sch"
$SpinupFileDirectory = "..\..\spinup"
$outfile = "..\outfile.txt"
$rawerror = "..\error.txt"
$outbin = $RunDirectory+"\spinup.bin"
if (Test-Path $outfile  ) {
  Remove-Item $outfile
}
$_="mlra_001_H_I_till_9428810.sch"

if (Test-Path $copyOut  ) {
  Remove-Item $copyOut
}
foreach($line in Get-Content $SpinupFileDirectory\$_) {
  Add-Content $copyOut -Value $line
    }



if (Test-Path $outbin  ) {
  Remove-Item $outbin
}
./DDcentEVI.exe -s spinup --site site.100 

if($LASTEXITCODE -ne 0){



}
else{
Write-Output SUCCESS! $_
}


