import re

total = 0
numbersAsWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('input.txt') as f:
    for line in f:
        line = line.rstrip()
        processed = ""
        i = 0
        while i < len(line):
            found = False
            for j, number in enumerate(numbersAsWords):
                if line[i:].startswith(number):
                    processed += str(j)
                    i += len(number)
                    found = True
                    break

            if not found:
                processed += line[i]
                i += 1

        first_digit = next((char for char in processed if char.isdigit()), None)
        last_digit = next((char for char in reversed(processed) if char.isdigit()), None)
        if first_digit and last_digit:
            total += int(first_digit + last_digit)  # combine first and last digit

print("TOTAL: ", total)