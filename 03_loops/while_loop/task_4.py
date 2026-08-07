"""Task 4"""

counter = 1
total = 0

while counter <= 5:
    user_number = int(input('Enter 5 numbers: '))
    counter += 1

    if user_number == 0:
        continue

    total += user_number

print(total)