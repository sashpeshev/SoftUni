record_in_second = float(input())
distance_in_meter = float(input())
one_meter_swim = float(input())

extra_time = distance_in_meter // 15 * 12.5
time = distance_in_meter * one_meter_swim + extra_time

if record_in_second > time:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    seconds_more = time - record_in_second
    print(f"No, he failed! He was {seconds_more:.2f} seconds slower.")
