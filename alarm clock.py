import time
CLEAR="\033[2J"
CLEAR8AND_RETURN="\033[H"
def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left=seconds - time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60
        print(f"{CLEAR8AND_RETURN}Alarm will sound in {minutes_left:02d}:{seconds_left:02d}")
minutes=int(input("how many minutes to wait? "))
seconds=int(input("how many seconds to wait? "))
tot_seconds=minutes*60+seconds
alarm(tot_seconds)
