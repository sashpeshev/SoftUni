n = int(input())

outer_dots = (n - 1) // 2
inner_dots = n - 2
dies = n

print("." * outer_dots + "#" * dies + "." * outer_dots)

for i in range(n -2):
    print("." * outer_dots + "#" + "." * inner_dots + "#" + "." * outer_dots)

outer_dots += 1
print("#" * outer_dots + "." * inner_dots + "#" * outer_dots)

outer_dots = 1
inner_dots = 2 * n - 5
for i in range(n - 2):
    print("." * outer_dots + "#" + "." * inner_dots + "#" + "." * outer_dots)
    outer_dots += 1
    inner_dots -= 2

print("." * outer_dots + "#" + "." * outer_dots)
