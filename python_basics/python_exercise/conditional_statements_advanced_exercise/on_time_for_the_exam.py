exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

if arrival_time > exam_time:
    print("Late")
elif exam_time >= arrival_time >= exam_time - 30:
    print("On time")
else:
    print("Early")

difference = abs(arrival_time - exam_time)
hours = difference // 60
minutes = difference % 60

if exam_time > arrival_time > exam_time - 60:
    print(f"{minutes} minutes before the start")
elif arrival_time <= exam_time - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif exam_time < arrival_time < exam_time + 60:
    print(f"{minutes} minutes after the start")
elif arrival_time >= exam_time + 60:
    print(f"{hours}:{minutes:02d} hours after the start")
