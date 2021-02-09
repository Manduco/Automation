import time, os
from playsound import playsound

One_Day_In_Seconds = 86400
Twelve_hours = One_Day_In_Seconds/2
Six_hours = Twelve_hours/2
Test_num = 500
One_Min = 60
One_Secound = 1
KeepRunning = True

def main():
    Ding_Every = int(One_Min)
    Reset_Timer = One_Min

    while (KeepRunning):

        Format_time = convert(Ding_Every)
        time.sleep(One_Secound)
        Ding_Every -= 1

        print('\033[H\033[J', end='')
        print("Time till Code Push ",end=" ")
        print(":",str(Format_time))

        if(Ding_Every == 0):
            
            Ding_Every = Reset_Timer
            playsound("ding.mp3",True)
            
# converts seconds
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

# __name__ 
if __name__=="__main__": 
    main()
