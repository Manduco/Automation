import datetime
import os.path, time

now = datetime.datetime.now()

print ("Current date and time : " +now.strftime("%Y-%m-%d %H:%M:%S"))

print("Last modified: %s" % time.ctime(os.path.getmtime("file.txt")))
print("Created: %s" % time.ctime(os.path.getctime("file.txt")))