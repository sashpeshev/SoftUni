n = int(input())

result = ""

a = 1
while a < 10:
    b = 1
    while b < 10:
        c = 1
        while c < 10:
            d = 1
            while d < 10:
                e = 1
                while e < 10:
                    f = 1
                    while f < 10:
                        if a * b * c * d * e * f == n:
                            result += str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + " "
                        f += 1
                    e += 1
                d += 1
            c += 1
        b += 1
    a += 1
print(result)
