import time, os, random

Two_Days = 86400 * 2
One_Day_In_Seconds = 86400
Twelve_hours = One_Day_In_Seconds / 2
Six_hours = Twelve_hours / 2
random_time_Selected = random.randrange(Six_hours, Two_Days)
Test_num = 10
One_Secound = 1
KeepRunning = True


def main():
    Count_At = int(10)
    while (KeepRunning):

        Format_time = convert(Count_At)
        time.sleep(One_Secound)
        Count_At -= 1

        print("\033[H\033[J", end="")
        print("Time till Code Push ", end=" ")
        print(":", str(Format_time))

        if (Count_At == 0):
            Count_At = random.randrange(Six_hours, Twelve_hours)
            os.system('python3 Auto_write.py')
            os.system('python3 Auto_push.py')


# converts seconds
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


# __name__
if __name__ == "__main__":
    main()
else:
    print("end")
