number = int(input())
edinici = number % 10
desetici = number // 10
texts = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
texts_desetici = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
if number < 20:
    print(texts[number])
elif number < 100:
    if edinici == 0:
        print(texts_desetici[desetici])
    else:
        print(texts_desetici[desetici]+" "+texts[edinici])
else:
    print("one hundred")
