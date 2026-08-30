
# """Task 1"""

# def create_profile(name, language="Python", level="Beginner"):

#     print()
#     print(f"Name: {name}")
#     print(f"Language: {language}")
#     print(f"Level: {level}")

# create_profile("Alex")
# create_profile("Alex", "Go")
# create_profile("Alex", "C++", "Advanced")


# """Task 2"""

# def calculate_price(price, quantity=1, discount=0):

#     result = price * quantity - (price * quantity * discount / 100)
#     return result

# print(calculate_price(100))
# print(calculate_price(100, 3))
# print(calculate_price(100, 3, 20))


# """Task 3"""

# def calculate_delivery(order_total, country="local", express=False):

#     delivery = 0

#     if country == "local":
#         delivery += 5
#     else:
#         delivery += 15

#     if express == True:
#         delivery += 10

#     if order_total >= 100:
#         delivery = 0

#     return  delivery
    
# print(calculate_delivery(50))
# print(calculate_delivery(50, "international"))
# print(calculate_delivery(50, "international", True))
# print(calculate_delivery(150, "international", True))


# """Task 4"""

# def filter_products(products, min_price=0):

#     found = False

#     for dct in products:
#         if dct["price"] >= min_price:
#             found = True
#             print(f"{dct["name"]}: {dct["price"]}")

#     if not found:
#         print("No products found.")

# print()

# filter_products([
#     {"name": "Keyboard", "price": 80},
#     {"name": "Mouse", "price": 35},
#     {"name": "Monitor", "price": 250},
#     {"name": "Headphones", "price": 120}
# ], 100)


# """Task 5"""

# def create_user(name, role="user", active=True):

#     user_dict = {"name": name, "role": role, "active": active}
#     return user_dict

# print(create_user("Alex"))
# print(create_user("Bob", "admin"))
# print(create_user("Charlie", active=False))
# print(create_user("David", role="moderator", active=False))


# """Final Mini-Program — Order Manager"""

# def create_order(product, quantity=1, priority=False):

#     order_dict = {"product": product, "quantity": quantity, "priority": priority}
#     return order_dict
    
# orders = []

# while True:
        
#     user_input_action = input("Choose an action:\n" \
           
#     "1 - Add order\n" \
#     "2 - Show orders\n" \
#     "3 - Show priority orders\n" \
#     "exit - Quit\n"
#     ).lower()

#     if user_input_action == "exit":
#         break
        
#     if user_input_action == "1":
#         print()
#         product = input("Enter product name: ")
#         add_quantity = input("Enter quantity: ")
#         order_is_priority = input("Is the order priority? (yes/no)").lower()

#         if add_quantity == "":
#             if order_is_priority == "yes":
#                 orders.append(create_order(product, priority=True))
#             else:
#                 orders.append(create_order(product))
#         else:
#             if order_is_priority == "yes":
#                 orders.append(create_order(product, int(add_quantity), priority=True))
#             else:
#                 orders.append(create_order(product, int(add_quantity)))

#         print()
#         print("Order added.")
#         print()

#     elif user_input_action == "2":
#         if orders:
#             for order in orders:
#                 print()
#                 for key, value in order.items():
#                     print(f"{key}: {value}")
#         else:
#             print("The order list is empty")

#     elif user_input_action == "3":
#         found = False
#         if orders:
#             for order in orders:
#                 if order["priority"]:
#                     found = True
#                     print()
#                     for key, value in order.items():
#                         print(f"{key}: {value}")
#         print()
#         if not found:
#             print("The priority order list is empty")

#     print()


    