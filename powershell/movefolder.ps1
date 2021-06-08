$RootPath = "C:\Users\arman\Desktop\testdir"

# Root path


# Get list of parent folders in root path

$ParentFolders = Get-ChildItem -path $RootPath -Recurse | ? { $_.PSIsContainer } | Select-Object FullName

# For each parent folder get all files recursively and move to parent, append number to file to avoid collisions
ForEach ($Parent in $ParentFolders) {
    Get-ChildItem -Path $Parent.FullName -Recurse | ForEach {
        $FileInc = 1
        Do {
            If ($FileInc -eq 1) { $MovePath = Join-Path -Path $Parent.FullName -ChildPath $.Name }
            Else { $MovePath = Join-Path -Path $Parent.FullName -ChildPath "$($.BaseName)($FileInc)$($.Extension)" }
            $FileInc++
        }
        While (Test-Path -Path $MovePath -PathType Leaf)
        Move-Item -Path $_.FullName -Destination $MovePath
    }
}

write-host $ParentFolders 