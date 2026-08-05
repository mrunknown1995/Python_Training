# """Task 1"""

# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))

# if first_num > second_num:
#     print(f'The greater number is {first_num}')
# elif second_num > first_num:
#     print(f'The greater number is {second_num}')
# elif first_num == second_num:
#     print('Numbers are equal')


# """Task 2"""

# age = int(input('How old are you? '))

# if age < 18:
#     print('Access denied')
# else:
#     print('Access granted')


# """Task 3"""

# temp = float(input('Enter temperature: '))

# if temp < 0:
#     print("It's freezing")
# elif temp < 21:
#     print("It's cool")
# else:
#     print("It's warm")


# """Task 4"""

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# num3 = int(input('Enter third number: '))

# greater_num = max(num1, num2, num3)

# print(greater_num)


# """Task 4 (alternative version)"""

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# num3 = int(input('Enter third number: '))

# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)


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

