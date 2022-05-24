import math

pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
hours = float(input())

filled_by_first_pipe = hours * first_pipe_flow
filled_by_second_pipe = hours * second_pipe_flow
total = filled_by_first_pipe + filled_by_second_pipe

in_percent = total / pool_volume * 100
in_percent_first_pipe = filled_by_first_pipe / total * 100
in_percent_second_pipe = filled_by_second_pipe / total * 100

if pool_volume >= total:
    print(f"The pool is {math.trunc(in_percent)}% full "
          f"Pipe 1: {math.trunc(in_percent_first_pipe)}%. "
          f"Pipe 2: {math.trunc(in_percent_second_pipe)}%.")
else:
    overflow = total - pool_volume
    print(f"For {hours} hours the pool overflows with {overflow} liters.")
