$eqruns = ".\spinup\"
$outdir = ".\fixedSpinups\"
$count=0
(Get-ChildItem -Path $eqruns -Filter '*.sch' -File) | ForEach-Object {
   
    $file = $_.FullName
    $do=$false
     $result = switch -File $file {
     { $_.Length -ge 80 } {
     $do=$true
     break
     }
     }
     $newlines=@()
     if($do){
     $result = switch -File $file {
     { $_.Length -ge 80 } {
      
        $subline = $_.subString(0,80)
        $index=$subline.LastIndexOf(',')+1
        $line1 = $_.subString(0,$index)
        $line2 = $_.subString($index)
        $newlines+=$line1
        $newlines+=$line2
      
        } 
        default { $newlines+=$_}    

     }
     $outname = $outdir+((Split-Path $file -leaf).Trim())
      Write-Host $outname
            $newlines | Out-File -Append  $outname
    }
    
 
    

  
}
  Write-Host $count