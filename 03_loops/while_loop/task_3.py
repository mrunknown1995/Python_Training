"""Task 3"""

password = 'python123'

while True:
    user_input = input('Enter your password: ')

    if user_input == password:
        print('Access granted!')
        break
