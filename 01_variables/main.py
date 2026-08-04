"""Task 1"""

name = 'John'
age = 30
city = 'Moscow'
height = 176
weight = 75

print(
    f'My name is {name} i am from' 
    f'{city}and i am {age}. My height is {height}'
    f'and my weight is {weight}.'
)


"""Task 2"""

name = input('Your name: ')
age = int(input('Your age: '))

print(f'Your name is {name} and your age is {age}')


"""Task 3"""

salary = 120000
food = 30000
gasoline = 40000
apartment = 20000
expenses = food + gasoline + apartment
the_rem_amount = salary - expenses

print(
    f'Salary = {salary}\n'
    f'Expenses = {expenses}\n'
    f'The remaining amount = {the_rem_amount}\n'
)


"""Task 4"""

salary = int(input('Enter your salary: '))
food = int(input('How much do you spend on food: '))
gasoline = int(input('How much do you spend on gasoline: '))
apartment = int(input('How much is your apartment: '))

expenses = food + gasoline + apartment
remaining_amount = salary - expenses

print(
    f'Salary = {salary}\n'
    f'Expenses = {expenses}\n'
    f'The remaining amount = {remaining_amount}\n'
)