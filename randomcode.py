import time, os

One_Day_In_Seconds = 86400
Test_num=100
One_Secound = 1
KeepRunning = True

def main():
    Count_At = 10

    while (KeepRunning):

        time.sleep(One_Secound)
        Count_At -= 1

        print('\033[H\033[J', end='')
        print("scounds till push",end=" ")
        print(":",str(Count_At))

        if(Count_At == 0):
            Count_At = 10
            os.system('python3 write.py')
          
      

  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main()
else:
    print("end") 