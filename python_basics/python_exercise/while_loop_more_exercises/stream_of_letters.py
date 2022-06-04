command = input()
code_one = "n"
code_two = "o"
code_three = "c"
sentence = ""

while command != "End":
    num = ord(command)
    if num in range(65, 91) or num in range(97, 123):
        char = chr(num)
        if char == "n" and code_one:
            code_one = ""
        elif char == "o" and code_two:
            code_two = ""
        elif char == "c" and code_three:
            code_three = ""
        else:
            sentence += char
    if not (code_one or code_two or code_three):
        code_one = "n"
        code_two = "o"
        code_three = "c"
        sentence += " "
        print(sentence, end="")
        sentence = ""
    command = input()
