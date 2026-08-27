
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