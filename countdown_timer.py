import time

def countdown_timer(h, m, s):
    while True:
        print(f"{h:02d}:{m:02d}:{s:02d}")
        time.sleep(1)
        if s > 0:
            s -= 1
        elif m > 0:
            m -= 1
            s += 59
        elif h > 0:
            h -= 1
            m += 59
            s += 59
        else:
            break

while True:
    time_tocount = input("Insert time to count down (h:m:s) ")
    time_matrix = [int(elem) for elem in time_tocount.split(':')]
    if len(time_matrix) != 3:
        print("You must enter all 3 values in the format (h:m:s)")
        continue
    elif max(time_matrix) <= 0 or min(time_matrix)<0:
        print("Values must be non-negative and at least one value must be positive")
        continue
    elif time_matrix[2] > 60 or time_matrix[1] > 60:
        print("Minute and second values cannot exceed the limit value of 59.")
        continue
    else:
        break

countdown_timer(time_matrix[0], time_matrix[1], time_matrix[2])
