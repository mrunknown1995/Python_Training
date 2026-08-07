"""Task 2"""

total = 0

while True:
    user_number = int(input('Type numbers one by one: '))

    if user_number == 0:
        break

    total += user_number

print(total)
