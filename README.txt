The Intent of this software is to auto push (code or any file) 
to github Repo at a given of time

-- Notes: is messure and used on secounds 

-- FILES required:
    Auto.py
    Write.py
    autopush.py

-- dependencies required/Installs required
    -Python3 installed
        Python Lib required
        - time, os >> Auto.py
        - git import Repo >> autopush.py
        - glob, os , datetime >> write.py

Secuirty Issus or concernc i Am aware of:
    -no try/catch for fail points
    -All 3 file must be in the same Dir 
    -Code does not check to see if changes were made it just pushes the code as is at the given time
    -once the code is ran force quiting the terminal is requiered to in the process

To rune the code vicieyr you are in the current Dir that files are in\
Enter: 'Python3 Auto.py' in a terminal
