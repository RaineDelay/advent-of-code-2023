total = 0
digits = []

with open("/home/raine/github/personal/advent-of-code-2023/1/input") as f:
    lines = f.readline()

    for line in lines:
        for char in line:
            if (char.isnumeric()):
                digits.append(char[0])
        total += (int)(digits[0] + digits[-1])
        digits = []
        
    print(total)