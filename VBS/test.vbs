
Dim fso, MyFile
Set fso = CreateObject("Scripting.FileSystemObject")
Set MyFile = fso.CreateTextFile("c:\testfile1.txt", True)
MyFile.WriteLine("This is a test.")
MyFile.Close
