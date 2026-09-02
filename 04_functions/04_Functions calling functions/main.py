
# """Task 1"""

# def calculate_total(price, quantity):
#     return price * quantity

# def print_order(price, quantity):

#     total = calculate_total(price, quantity)

#     print(f"Price: {price}")
#     print(f"Quantity: {quantity}")
#     print(f"Total: {total}")

# print_order(100, 3)


# """Task 2"""

# def order_price_calc(product_price, quantity):
#     return product_price * quantity
    
# def input_price_and_quantity():
    
#     user_input_price = int(input("Enter price: "))
#     user_input_quantity = int(input("Enter quantity: "))

#     total_price = order_price_calc(user_input_price, user_input_quantity)
#     return total_price

# def show_final_result():

#     total_price = input_price_and_quantity()

#     if total_price >= 1000:
#         final_price = total_price - total_price * 10 / 100
#     else:
#         final_price = total_price

#     print(f"total: {total_price}")
#     print(f"Final price: {final_price}")

# show_final_result()


# """Task 3"""

# def calc_total(product_1, product_2, product_3):
#     return product_1 + product_2 + product_3

# def enter_product():
#     user_input_product_1 = int(input("Enter product 1 price: "))
#     user_input_product_2 = int(input("Enter product 2 price: "))
#     user_input_product_3 = int(input("Enter product 3 price: "))

#     total_price = calc_total(user_input_product_1, user_input_product_2, user_input_product_3)
#     print(f"Subtotal: {total_price}")
#     return total_price

# def calc_discount():
#     total_price = enter_product()
#     discount = 0

#     if total_price >= 1000 and total_price <= 1999:
#         discount = total_price * 10 / 100
#         final_price = total_price - total_price * 10 / 100
#     elif total_price >= 2000:
#         discount = total_price * 20 / 100
#         final_price = total_price - total_price * 20 / 100
#     else:
#         final_price = total_price

#     print(f"Discount: {discount}")
#     return final_price

# def calc_delivery_and_show_the_result():

#     final_price = calc_discount()
#     delivery = 200

#     if final_price < 1500:
#         final_price += delivery
#     else:
#         delivery = 0

#     print(f"Delivery: {delivery}")
#     print(f"Final price: {final_price}")

# calc_delivery_and_show_the_result()
