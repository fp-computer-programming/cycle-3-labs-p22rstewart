# Author: Ryan (AMDG) 10/6/21

points = int(input("# of points scored: "))
if points < 9:
    print("you did not earn a medal")
elif points <= 11:
    print("you earned a bronze medal")
elif points <= 14:
    print("you earned a silver medal")
elif points >= 15:
    print("you earned a gold medal")
