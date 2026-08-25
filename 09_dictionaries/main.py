
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
    