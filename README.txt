[-]Intent of this software is to 
   auto push (code or any file) 
   to github Repo at a given of time

[-]What it does:
    Auto.py >> loops till Var [Count_At] is Equal to 0 
               then calls Write.py and Auto.py respectively
    Write.py >> Opens a file with name stored in [File_Name] 
                and writes the time is was opened
    Auto.py >> Pushes a *Hardcoded* string "file.txt" to github repo

[-]Code ran correctly 
    - At: 2020-12-14 16:19:58 
    - On: Mac OS Big Sur 11.0.1

[-] FILES required:
    Auto.py
    Write.py
    autopush.py
[-] dependencies required/Installs required
    -Python3 installed
        Python Lib required
        - time, os >> Auto.py
        - git import Repo >> autopush.py
        - glob, os , datetime >> write.py
    
    # pip install GitPython

[-]security issues or concerns i Am aware of:
    -no try/catch for fail points
        there should be try/catch at all functionas calls
    -All 3 file must be in the same Dir 
    -Code does not check to see if changes were made it just pushes the code as is at the given time
    -once the code is ran force quiting the terminal is requiered to in the process
    -More security resceah most be done on git repo library used in autppush.py

[-] Notes: 
    -Time is measured and used in secounds and 
     in the Convert() Func in Auto.py File
    -How to run: run the code Via terminal you are in the current 
     'Python3 Auto.py' in a terminal
