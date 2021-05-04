[DateTime]$start_time = "2021-04-15 00:00:00"
[DateTime]$end_time = "2021-05-03 23:59:59"
$desfolder = "C:\Users\arman\Desktop\testdir"
$TESTDir = "C:\Users\arman\Desktop\testdir"

Get-ChildItem -path $TESTDir -Recurse -File | Foreach 
{
    $FileInc = 1
  
    if ($.lastwritetime -ge $start_time -and $.lastwritetime -le $end_time) {
        If ($FileInc -eq 1) { 
            move-item $.fullname $desfolder 
        }
        Else { 
            $MovePath = Join-Path -Path $desfolder "$($.BaseName)($FileInc)$($.Extension)" 
            Rename-Item -Path "c:\logfiles\daily_file.txt" -NewName "monday_file.txt"
            #change stuff here
       
        }
    }
}

