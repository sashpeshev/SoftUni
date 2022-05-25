number = int(input())
stotici = number // 100
edinici = (number - stotici * 100) % 10
desetici = (number - stotici * 100) // 10
texts = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
texts_desetici = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
if number >= 100:
    print(texts[stotici] + " hundred", end="")
    if not (desetici == 0 and edinici == 0):
        print(" and ", end="")
    number -= stotici * 100

if number == 0 and stotici == 0:
    print("zero")
elif number < 20:
    print(texts[number])
elif number < 100:
    if edinici == 0:
        print(texts_desetici[desetici])
    else:
        print(texts_desetici[desetici]+" "+texts[edinici])