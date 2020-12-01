import glob, os
import datetime
from os import path
#os import docs https://docs.python.org/3/library/os.html

global File_Name , Files_found
File_Name = "File_Name_Here"

Folders_found = 0
Files_found = 0
Num_of_folders_to_parse= 5
Dir_Root = "testfile"
Dir_To_Search = "testfile"
Dir_Sub_Wildcard = "*"
Dir_Return = ".."
Dir_current = "whateve"

def stats_Update():

    now = datetime.datetime.now()
    format_date = now.strftime("%Y-%m-%d %H:%M:%S")
    stats = open("file.txt","a+")
    stats.write(" "+ Dir_current +" Dir contains "+str(Files_found)+" Ran on: "+format_date+"  \n")
    stats.close()
    print("file.txt has been updated")

print(os.path.abspath(os.curdir))
Dir_current = os.path.abspath(os.curdir)

print("\n --------------Start----------------")

Dir_current = Dir_current.split("/", 5)[-1]
for File_Name in glob.glob(Dir_Sub_Wildcard):
    Files_found += 1
    
stats_Update()
    

