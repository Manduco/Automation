#made my manduco

[DateTime]$start_time = "2021-04-15 00:00:00"
[DateTime]$end_time = "2021-05-03 23:59:59"
$desfolder = "C:\Users\arman\Desktop\testdir"
$Root = "C:\Users\arman\Desktop\testdir"

$i = 0 

Get-ChildItem -path $Root -Recurse -File | ForEach-Object -Process { if ($_.lastwritetime -ge $start_time -and $_.lastwritetime -le $end_time ) {


        #rename file function here
        #just move file function
        $currentFile_Name = [string]$_
        #write-host $currentFile_Name
        Change_nameOfFile $currentFile_Name

        $i = $i + 1
    }

}


Function Change_nameOfFile($currentFile_Name) {

    #$New_name = -join($Old_name , " ", "world");
    #Rename-Item -Path "c:\logfiles\daily_file.txt" -NewName "monday_file.txt"

    write-host $currentFile_Name 

}





