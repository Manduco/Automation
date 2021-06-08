#made my manduco

[DateTime]$start_time = "2021-04-15 00:00:00"
[DateTime]$end_time = "2021-11-03 23:59:59"
$desfolder = "C:\Users\arman\Desktop\testdir"
$Root = "C:\Users\arman\Desktop\testdir"

$i = 0
$number_of_Files = 0

Get-ChildItem -path $Root -Recurse -File | ForEach-Object -Process { if ($_.lastwritetime -ge $start_time -and $_.lastwritetime -le $end_time ) {


        #rename file function here
        #just move file function
        $currentFile_Name = [string]$_.Basename
        $currentFile_Name_full = [string]$_.FullName

        #Change_nameOfFile $currentFile_Name

        $New_name = -join ($currentFile_Name , "_", $i , $_.extension);
        $New_fullpath = -join ("C:\Users\arman\Desktop\testdir\" , $New_name);


        #write-host $currentFile_Name_full
        write-host $New_name
        #write-host $New_fullpath


        #Rename-Item  -Path $currentFile_Name_full -NewName {$_.Basename.Replace("old","new") + $_.extension}
        #Rename-Item -Path $currentFile_Name_full -NewName $New_fullpath
        #Rename-Item -path $currentFile_Name_full -newname ($_.Basename.Replace("OLD")+ $_.Extension)

        #Move-Item -Path $currentFile_Name_full -Destination $desfolder 

        $i = $i + 1

    }
}

