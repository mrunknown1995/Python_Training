
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


# """Task 4"""

# def run_session():
#     attempts = 0
    
#     def add_attempt():
#         nonlocal attempts
#         attempts += 1

#     add_attempt()
#     add_attempt()
#     add_attempt()
#     print(attempts)

# run_session() 


# """Task 5"""

# def login_system():
#     password = "python123"
#     attempts = 3

#     def check_password(user_password):
#         nonlocal attempts

#         if password == user_password:
#             return True
#         else:
#             attempts -= 1
#             return False

#     while True:
#         user_pass = input("Enter password: ")
#         res = check_password(user_pass)

#         if attempts == 0:
#             print("Wrong password.")
#             print("Access denied.")
#             break

#         if res:
#             print("Access granted.")
#             break

#         else:
#             print("Wrong password.")
#             print(f"Attempts left: {attempts}")
#             print()

# login_system()


# """Scope Mini-Program — Study Session Manager"""

# total_sessions = 0

# def total_session():
#     global total_sessions
#     total_sessions += 1

# def start_session():
#     tasks_completed = 0
#     session_points = 0

#     def count_points(points):
#         nonlocal tasks_completed
#         nonlocal session_points

#         if points <= 0:
#             print("Invalid points.")
#         else:
#             tasks_completed += 1
#             session_points += points
#             print("Tasks completed.")

#     while True:

#         user_input_action = input("Choose an action:\n" \
           
#         "1 - Complete task\n" \
#         "2 - Show session stats \n" \
#         "3 - Finish session\n"
#         ).lower()

#         if user_input_action == "1":
#             user_how_many_points = int(input("How many points did you get for completed task? "))
#             count_points(user_how_many_points)

#         elif user_input_action == "2":
#             print(f"Task completed: {tasks_completed}")
#             print(f"Session points: {session_points}")

#         elif user_input_action == "3":
#             print("Session finished.")
#             print(f"Task completed: {tasks_completed}")
#             print(f"Session points: {session_points}")
#             total_session()

#             break

# while True:

#     user_input_action = input("Choose an action:\n" \
           
#     "1 - Start study session\n" \
#     "2 - Show total sessions \n" \
#     "exit - Quit\n"
#     ).lower()

#     if user_input_action == "exit":
#         break

#     if user_input_action == "1":
#         start_session()

#     elif user_input_action == "2":
#         print(f"Total completed sessions: {total_sessions}")