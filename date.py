import datetime, os.path, time, json

FileToTest = "file.txt"
now = datetime.datetime.now()
file_lastdateM = " -date-"

#file data on files I files i want tracked
#print ("Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))
#file_lastdateM = str(time.ctime(os.path.getmtime(FileToTest)))
#print(FileToTest +" Created: %s" % time.ctime(os.path.getctime(FileToTest)))
#print(file_lastdateM)

with open('date.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)
#datetime.timedelta(now, )
# x = with subkey ie while file

data["Tracking_files"]["files"][0]["Last_Date_Mod"] = file_lastdateM
print(data["Tracking_files"]["files"][0]["file_name"])
print(data["Tracking_files"]["files"][0]["Last_Date_Mod"])

#write update json to file
with open('data1.txt', 'w') as outfile:
    json.dump(data,outfile, indent=2)