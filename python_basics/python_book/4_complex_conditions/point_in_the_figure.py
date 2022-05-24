h = int(input())
x = int(input())
y = int(input())

in_rectangle1 = (x > 0) and (x < 3 * h) and (y > 0) and (y < h)
in_rectangle2 = (x > h) and (x < 2 * h) and (y >= h) and (y < 4 * h)

out_rectangle1 = (x < 0) or (x > 3 * h) or (y < 0) or (y > h)
out_rectangle2 = (x < h) or (x > 2 * h) or (y < h) or (y > 4 * h)

if in_rectangle1 or in_rectangle2:
    print("inside")
elif out_rectangle1 and out_rectangle2:
    print("outside")
else:
    print("border")
