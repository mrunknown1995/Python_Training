
# """Task 1"""

# language = "Python"

# def show_language():
#     global message
#     message = "I'm learning"
#     print(f"{message} {language}")

# show_language()


# """Task 2"""

# score = 100

# def change_score():

#     score = 50
#     print(score)

# change_score()
# print(score)


# """Task 3"""

# balance = 1000

# def deposit(amount):

#     global balance

#     if amount <= 0:
#         print("Invalid amount.")
#     else:
#         balance += amount
#         print("Money deposited.")

# def withdraw(amount):

#     global balance

#     if amount > balance:
#         print("Not enough money.")
#         print(f"Current balance: {balance}")

#     elif amount <= 0:
#         print("Invalid amount.")
#     else:
#         balance -= amount
#         print("Money withdrawn.")

# while True:
        
#     user_input_action = input("Choose an action:\n" \
           
#     "1 - Deposit\n" \
#     "2 - Withdraw\n" \
#     "3 - Show balance\n" \
#     "exit - Quit\n"
#     ).lower()

#     if user_input_action == "exit":
#         break

#     if user_input_action == "1":
#         user_deposit_amount = int(input("Enter amount: "))

#         deposit(user_deposit_amount)

#     elif user_input_action == "2":
#         user_withdraw_amount = int(input("Enter amount: "))

#         withdraw(user_withdraw_amount)

#     elif user_input_action == "3":
#         print(f"Current balance: {balance}")
