
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


# """Task 4"""

# def analyze_prices(*args):

#     total_price = 0
#     cheap = args[0]
#     expensive = args[0]
    
#     for num in args:
#         total_price += num

#         if num > expensive:
#             expensive = num

#         elif num < cheap:
#             cheap = num

#     return total_price, cheap, expensive

# print(analyze_prices(100, 250, 50, 400))
# # (800, 50, 400)
# print(analyze_prices(75))
# # (75, 75, 75)
# print(analyze_prices(100, 100, 200, 200))
# # (600, 100, 200)
# print(analyze_prices(-100, -50, -200))


# """Task 5"""

# def show_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# show_profile(name="John", age=30, language="Python")
# show_profile(city="Moscow", job="Developer")


# """Task 6"""

# def filter_data(**kwargs):

#     new_dict = {}

#     for key, value in kwargs.items():
#         if value is not None:
#             new_dict[key] = value

#     return new_dict

# print(filter_data(name="John", age=30, city=None, language="Python"))
# # {'name': 'John', 'age': 30, 'language': 'Python'}
# print(filter_data(email=None, phone=None))
# # {}
# print(filter_data())
# # {}


# """Task 7"""

# def calculate_stats(**kwargs):

#     new_dict = {"total": 0, "count": 0, "average": 0}
#     total = 0
#     count = 0

#     for key in kwargs:
#         total += kwargs[key]
#         count += 1

#         new_dict["total"] = total
#         new_dict["count"] = count

#     if kwargs:
#         new_dict["average"] = total / len(kwargs)

#     return new_dict
    
# print(calculate_stats(math=80, english=90, python=100))
# # {'total': 270, 'count': 3, 'average': 90.0}
# print(calculate_stats(task1=10, task2=20))
# # {'total': 30, 'count': 2, 'average': 15.0}
# print(calculate_stats())
# # {'total': 0, 'count': 0, 'average': 0}


# """Mini-Program — Game Match Report"""

# def game_match_report(*args, **kwargs):

#     players = 0
#     total_score = 0
#     average_score = 0
#     highest_score = args[0]
#     lowest_score = args[0]

#     for item in args:
#         players += 1
#         total_score += item

#         if item > highest_score:
#             highest_score = item

#         elif item < lowest_score:
#             lowest_score = item

#     if args:
#             average_score = total_score / players

#     match_info_key = ""

#     for key, value in kwargs.items():
#         match_info_key += f"{key.capitalize()}: {value}\n"

#     return \
#     f"MATCH REPORT\n\n\
# {match_info_key}\n\
# Players: {players}\n\
# Total score: {total_score}\n\
# Average score: {average_score}\n\
# Highest score: {highest_score}\n\
# Lowest score: {lowest_score}"

# report = game_match_report(120, 85, 200, 150, map="Desert", mode="Team Deathmatch", duration=18)

# print()
# print(report)
