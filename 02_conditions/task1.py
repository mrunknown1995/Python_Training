"""Task 1"""

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))

if first_num > second_num:
    print(f'The greater number is {first_num}')
elif second_num > first_num:
    print(f'The greater number is {second_num}')
elif first_num == second_num:
    print('Numbers are equal')
