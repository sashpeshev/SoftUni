n = int(input())
fact = 1

while True:
    fact = fact * n
    n -= 1
    if not n > 1:
        break
print(fact)
