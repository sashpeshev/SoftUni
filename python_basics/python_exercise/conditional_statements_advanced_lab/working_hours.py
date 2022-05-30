pm_am = int(input())
week_day = input()

if 10 <= pm_am <= 18 and week_day != "Sunday":
    print("open")
else:
    print("closed")
