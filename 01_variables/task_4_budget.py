"""Task 4"""

salary = int(input('Enter your salary: '))
food = int(input('How much do you spend on food: '))
gasoline = int(input('How much do you spend on gasoline: '))
apartment = int(input('How much is your apartment: '))

expenses = food + gasoline + apartment
remaining_amount = salary - expenses

if expenses > salary:
    print('the budget is exceeded')

else:
    print(
        f'Salary = {salary}\n'
        f'Expenses = {expenses}\n'
        f'The remaining amount = {remaining_amount}\n'
    )
