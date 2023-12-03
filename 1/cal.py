with open("test_input.txt") as f:
    lines = f.readlines()
    total = 0
    digits = []

    for line in lines:
        for char in line:
            if (char.isnumeric()):
                digits.append(char[0])
                
        total += int(digits[0] + digits[-1])
        digits = []

    print(total)
