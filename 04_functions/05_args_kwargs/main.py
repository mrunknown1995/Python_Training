
# """Task 1"""

# def calculate_sum(*args):
#     res = 0

#     for i in args:
#         res += i
#     return res

# print(calculate_sum(10, 20))
# # 30

# print(calculate_sum(1, 2, 3, 4, 5))
# # 15

# print(calculate_sum(100))
# # 100


# """Task 2"""

# def pos_or_neg_nums(*args):

#     pos_nums = 0
#     neg_nums = 0

#     for i in args:
#         if i > 0:
#             pos_nums += 1
#         elif i < 0:
#             neg_nums += 1

#     return len(args), pos_nums, neg_nums

# print(pos_or_neg_nums(10, -5, 0, 7, -2))
# # (5, 2, 2)

# print(pos_or_neg_nums(1, 2, 3))
# # (3, 3, 0)

# print(pos_or_neg_nums(-10, -20))
# # (2, 0, 2)

# print(pos_or_neg_nums(10, 10, -5, -5))


# """Task 3"""

# def find_largest(*args):

#     largest_number = args[0]

#     for i in args:
#         if i > largest_number:
#             largest_number = i

#     return largest_number

# print(find_largest(5, 12, 3, 20, 8))
# # 20
# print(find_largest(-10, -3, -25, -7))
# # -3
# print(find_largest(100))
# # 100
# print(find_largest(7, 7, 2, 7))
# # 7
