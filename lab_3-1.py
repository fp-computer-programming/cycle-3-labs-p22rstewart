# Author: Ryan (AMDG) 10/6/21

points = int(input("# of points scored: "))
if points < 9:
    print("you did not earn a medal")
else:
    if points <= 11:
        print("you earned a bronze medal")
    else:
        if points <= 14:
            print("you earned a silver medal")
        else:
            if points >= 15:
                print("you earned a gold medal")
