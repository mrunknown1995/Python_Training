"""Task 5"""

while True:
    user_number = int(input('Enter a number: '))

    if user_number == 0:
        break
    elif user_number % 2 == 0:
        print('even')
    else:
        print('odd')