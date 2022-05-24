n = int(input())

tens = n - n % 10
single = n % 10

tens_in_word = ""
singles_in_word = ""
result = ""

if single == 0:
    singles_in_word = "zero"
elif single == 1:
    singles_in_word = "one"
elif single == 2:
    singles_in_word = "two"
elif single == 3:
    singles_in_word = "three"
elif single == 4:
    singles_in_word = "four"
elif single == 5:
    singles_in_word = "five"
elif single == 6:
    singles_in_word = "six"
elif single == 7:
    singles_in_word = "seven"
elif single == 8:
    singles_in_word = "eight"
elif single == 9:
    singles_in_word = "nine"

if tens == 10:
    if single == 0:
        singles_in_word = "ten"
    elif single == 1:
        singles_in_word = "eleven"
    elif single == 2:
        singles_in_word = "twelve"
    elif single == 3:
        singles_in_word = "thirteen"
    elif single == 4:
        singles_in_word = "fourteen"
    elif single == 5:
        singles_in_word = "fifteen"
    elif single == 6:
        singles_in_word = "sixteen"
    elif single == 7:
        singles_in_word = "seventeen"
    elif single == 8:
        singles_in_word = "eighteen"
    elif single == 9:
        singles_in_word = "nineteen"
elif tens == 20:
    tens_in_word = "twenty"
elif tens == 30:
    tens_in_word = "thirty"
elif tens == 40:
    tens_in_word = "forty"
elif tens == 50:
    tens_in_word = "fifty"
elif tens == 60:
    tens_in_word = "sixty"
elif tens == 70:
    tens_in_word = "seventy"
elif tens == 80:
    tens_in_word = "eighty"
elif tens == 90:
    tens_in_word = "ninety"
elif tens == 100:
    tens_in_word = "one hundred"


if n < 20:
    result = singles_in_word
elif n >= 20 and single == 0:
    result = tens_in_word
else:
    result = tens_in_word + " " + singles_in_word

print(result)
