
# """Task 1"""

# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# user_prog_lang = input("Enter your programming language: ")

# user_info = {
#     "name": user_name,
#     "age": user_age,
#     "language": user_prog_lang
# }

# print()
# print("--- User Profile ---")
# print(f"Name: {user_info["name"]}")
# print(f"Age: {user_info["age"]}")
# print(f"Language: {user_info["language"]}")


# """Task 2"""

# user = {
#     "name": "Alex",
#     "age": 25,
#     "language": "Python"
# }

# new_age = input("Enter new age: ")
# user["age"] = new_age

# user_city = input("Enter your city: ")
# user["city"] = user_city

# print()
# print("--- Updated Profile ---")
# print(f"Name: {user["name"]}")
# print(f"Age: {user["age"]}")
# print(f"Language: {user["language"]}")
# print(f"City: {user["city"]}")


# """Task 3"""

# stock = {
#     "keyboard": 5,
#     "mouse": 8,
#     "monitor": 3
# }

# user_input_product = input("What product do you want to buy? ")

# if user_input_product in stock:
#     print(f"Available: {stock[user_input_product]}")

#     user_input_amount = int(input("How many do you want to buy? "))
#     new_quantity = stock[user_input_product] - user_input_amount
#     stock[user_input_product] = new_quantity

#     print(f"Remaining: {new_quantity}")

# else:
#     print("Product not found.")

# print(stock)


# """Task 4"""

# grades = {
#     "Alice": 85,
#     "Bob": 72,
#     "Charlie": 91,
#     "David": 68
# }

# accum = 0

# for key, value in grades.items():
#     print(f"{key}: {value}")
#     accum += value

# average_grade = accum / len(grades.items())
# print(f"Average grade: {average_grade}")


# """Task 5"""

# phone_book = {
#     "Alice": "555-1234",
#     "Bob": "555-5678",
#     "Charlie": "555-9012"
# }

# find_person = input("Enter a name: ")

# if find_person in phone_book:
#     print(f"{find_person}'s phone number: {phone_book[find_person]}")
# else:
#     print("The contact wasn't found.")

#     add_new_person = input(f"Would you like to add {find_person}? ").lower()

#     if add_new_person == "yes":
#         add_phone_number = input(f"Enter {find_person}'s phone number: ")
#         phone_book[find_person] = add_phone_number

#         print()
#         print("Updated phone book:")

#         for key, value in phone_book.items():
#             print(f"{key}: {value}")


# """Task 6"""

# students = {
#     "Alice": 85,
#     "Bob": 72,
#     "Charlie": 91,
#     "David": 68
# }

# while True:
    
#     user_input = input("Enter student name (or 'exit'): ")

#     if user_input == "exit":
#         break
#     elif user_input in students:
#         print(f"{user_input}'s grade is {students.get(user_input)}")
#     else:
#         print("Student not found.")


# """Task 7"""

# inventory = {
#     "keyboard": 5,
#     "mouse": 8,
#     "monitor": 3,
#     "headphones": 6
# }

# while True:

#     user_input = input("Enter a product to remove (or 'exit'): ").lower()

#     if user_input == "exit":
#         break

#     elif user_input in inventory:
#         inventory.pop(user_input)
#         print()
#         print(f"Removed: {user_input}")

#         print()
#         print("Current inventory:")

#         for key, value in inventory.items():
#             print(f"{key}: {value}")

#         print()

#     else:
#         print("Product not found.")


# """Task 8"""

# students = [
#     {
#         "name": "Alice",
#         "age": 21,
#         "grade": 85
#     },
#     {
#         "name": "Bob",
#         "age": 23,
#         "grade": 72
#     },
#     {
#         "name": "Charlie",
#         "age": 20,
#         "grade": 91
#     }
# ]

# accum = 0

# for dct in students:
#     print()

#     for key, value in dct.items():
#         print(f"{key.capitalize()}: {value}")

#     accum += dct["grade"]

# average_grade = accum / len(students)

# print()

# user_input = input("Enter a student name: ")
# print()

# found = False

# for dct in students:

#     if dct["name"] == user_input:
#         print("Student found!")

#         found = True

#         for key, value in dct.items():
#             print(f"{key.capitalize()}: {value}")

#         break

# if not found:
#     print("Student not found.")

# print()
# print(f"Average grade: {average_grade}")