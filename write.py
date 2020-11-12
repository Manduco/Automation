# to run the scirp place this scirpt,,
# in dir higher then the files you..
# which to convert
# by Armando Zincke

import glob, os
import datetime
from os import path
#os import docs https://docs.python.org/3/library/os.html

global File_Name , Files_found
File_Name = "File_Name_Here"
#define vars
Folders_found = 0
Files_found = 0
Num_of_folders_to_parse= 5


Dir_Root = "testfile"
Dir_To_Search = "testfile"
Dir_Sub_Wildcard = "*"
Dir_Return = ".."
Dir_current = "whateve"

User_answer=''


# define Func Here

def stats_Update():

    now = datetime.datetime.now()
    format_date = now.strftime("%Y-%m-%d %H:%M:%S")
    stats = open("file.txt","a+")
    stats.write("in "+ Dir_current +" contains "+str(Files_found)+" on: "+format_date+"  \n")
    stats.close()
    print("file.txt has been updated")


# Scirpt process Below {

#changes current working dir
print(os.path.abspath(os.curdir))
Dir_current = os.path.abspath(os.curdir)
#os.chdir(Dir_Root) #change dir if needed
#Print_below_shows_current_dir_the_script_is_Working_in_
#print(os.path.abspath(os.curdir))

print("\n --------------Start----------------")
#---IMPORTANT DIR MGT
#Dir_current.split("/", 5)[-1]
#^ SHOWS current working folder wont always work uses delimilter
Dir_current = Dir_current.split("/", 5)[-1]

for File_Name in glob.glob(Dir_Sub_Wildcard):

    Files_found += 1
    #Dir_current.split("/", 1)[-1]
    #print(" -- "+File_Name)
    #changes current working dir
    #os.chdir(folder)
    #print("\n Current Directory" + " >>> "+Dir_Root+"/"+"---| ")

    #find all .WAV in current dir
    #for file in glob.glob("*.wav"):
        #print(" -- "+file)
        #Files_found += 1
        #loop ends
    #find all .mp3 in current dir


#what if we have mp3s's in the dir?
stats_Update()
    #os.chdir(Dir_Return)


# } Scirpt process end
