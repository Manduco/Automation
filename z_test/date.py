import datetime, os.path, time, json

FileToTest = "file.txt"
CurrentDate = str(datetime.datetime.now())
LastDayRan= "-date-"
file_lastdateM = "-date-"
file_madeOn = "-startdate-"
file_Datecreated = "-dateMade-"

#file data on files I files i want tracked
file_lastdateM = str(time.ctime(os.path.getmtime(FileToTest)))
file_Datecreated = str(time.ctime(os.path.getctime(FileToTest)))
#print(FileToTest +" Created: %s" % time.ctime(os.path.getctime(FileToTest)))
#print(file_lastdateM)
#test
with open('date.json') as f:
  data = json.load(f)

print("sricpt last ran on: "+data["Tracking_files"]["Date_last_ran"])

data["Tracking_files"]["files"][0]["Last_Date_Mod2"] = data["Tracking_files"]["files"][0]["Last_Date_Mod"] 
data["Tracking_files"]["files"][0]["Last_Date_Mod"] = file_lastdateM
data["Tracking_files"]["files"][0]["Date_created"] = file_Datecreated
data["Tracking_files"]["Date_last_ran"] = CurrentDate

print(data["Tracking_files"]["files"][0]["file_name"])
print(data["Tracking_files"]["files"][0]["Last_Date_Mod"])

#write update json to file
with open('date.json', 'w') as outfile:
    json.dump(data,outfile, indent=2)
 
def compare():
  print("just_testing")