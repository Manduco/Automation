https://www.automateexcel.com/vba/call-function-from-a-sub/
https://github.com/andreafortuna-org/VBAIPFunctions/blob/master/IPFunctions.vba

'===================================================
'   IpSubnetLen
'   Source: https://github.com/andreafortuna-org/VBAIPFunctions/blob/master/IPFunctions.vba
'===================================================
' Return the mask len from a subnet
Function IpSubnetLen(ByVal ip As String)
    Debug.Print ip
End Function

Sub read_IP()

    Dim IP_Array(8)
    StartingRow = 2
    'might need to change the decl for StartingRow

        For i = 1 To 8
            IP_Array(i - 1) = Cells(StartingRow, i).Value
            Debug.Print GrabIPLeftlimit
            Debug.Print IP_Array(i - 1)
        Next i

    IpSubnetLen ("test")
    Debug.Print
End Sub


