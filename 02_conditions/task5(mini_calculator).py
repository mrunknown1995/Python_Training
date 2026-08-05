"""Task 5 (Mini calculator)"""

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

action = input('Select one operation from +-*/: ')
if action == '+':
    print(num1 + num2)
elif action == '-':
    print(num1 - num2)
elif action == '*':
    print(num1 * num2)
elif action == '/':
    print(num1 // num2)
else:
    print('The program does not support this symbol... ')

