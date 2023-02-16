

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
Get-ChildItem $SpinupFileDirectory -Filter *.sch |
Foreach-Object{

if (Test-Path $copyOut  ) {
  Remove-Item $copyOut
}
foreach($line in Get-Content $SpinupFileDirectory\$_) {
  Add-Content $copyOut -Value $line
    }



if (Test-Path $outbin  ) {
  Remove-Item $outbin
}
./DDcentEVI.exe -s spinup --site site.100 *>&1 > $rawerror

if($LASTEXITCODE -ne 0){

Write-Output error $_
Add-Content -path $outfile -value $_
$cont = ""
gc $rawerror | % { if($_ -cmatch "ERROR") {$cont+=$_}}


Add-Content -path $outfile -value $cont


}
else{
Write-Output SUCCESS! $_
}

if (Test-Path $rawerror  ) {
  Remove-Item $rawerror
}

}