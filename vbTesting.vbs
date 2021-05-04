
Sub read_IP()

    Dim IP_Array(8)
    StartingRow = 2
    'might need to change the decl for StartingRow

        For i = 1 To 8
            IP_Array(i - 1) = Cells(StartingRow, i).Value
            'Debug.Print GrabIPLeftlimit
           'Debug.Print IP_Array(i - 1)
        Next i

    'Debug.WriteLine("s")
    'IpSubnetLen(2333)
    Wscript.Echo "Like this?"
End Sub


read_IP()