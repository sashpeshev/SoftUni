n = int(input())

dots = n + 1
underscores = 2 * n + 1

print("{0}{1}{0}".format("." * dots, "_" * underscores))

underscores -= 2
dots -= 1
for i in range(n):
    print("{0}//{1}\\\\{0}".format("." * dots, "_" * underscores))
    dots -= 1
    underscores += 2

dots += 1
print("//{0}STOP!{0}\\\\".format("_" * ((underscores - 5) // 2)))

for i in range(n):
    print("{0}\\\\{1}//{0}".format("." * i, "_" * underscores))
    underscores -= 2
