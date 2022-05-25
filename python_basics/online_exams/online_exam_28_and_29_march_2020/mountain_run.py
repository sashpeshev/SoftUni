record_in_second = float(input())
distance_in_meter = float(input())
one_meter_climbs = float(input())

extra_time = distance_in_meter // 50 * 30
time = distance_in_meter * one_meter_climbs + extra_time

if record_in_second > time:
    print(f"Yes! The new record is {time:.2f} seconds.")
else:
    seconds_more = time - record_in_second
    print(f"No! He was {seconds_more:.2f} seconds slower.")
