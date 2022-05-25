startnum = input()
finalnum = input()
output = ""

for a in range(int(startnum[0]), int(finalnum[0]) + 1):
    for b in range(int(startnum[1]), int(finalnum[1]) + 1):
        for c in range(int(startnum[2]), int(finalnum[2]) + 1):
            for d in range(int(startnum[3]), int(finalnum[3]) + 1):
                if a % 2 == 1 and b % 2 == 1 and c % 2 == 1 and d % 2 == 1:
                    output += f"{a}{b}{c}{d} "

print(output)
