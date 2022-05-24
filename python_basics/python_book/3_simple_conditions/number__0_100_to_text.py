# numbers from 0 to 100 to text
n = int(input())

tens = n - n % 10
single = n % 10
hundreds = n // 100

dic_tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
dic_single = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
              9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
              16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

if n < 20:
    print(dic_single[n])
elif n < 100:
    if single == 0:
        print(dic_tens[tens])
    else:
        print(dic_tens[tens], dic_single[single])
else:
    temp = f"{dic_single[hundreds]} hundred "
    tens = n - 100 * (n // 100)
    if tens % 10 != 0:
        if tens < 20:
            temp += f"{dic_single.get(tens, '')}"
        else:
            temp += f"{dic_tens.get(tens - tens % 10, '')} "
            temp += f"{dic_single.get(tens % 10, '')}"

    print(temp)

