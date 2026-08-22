
# """Task 1"""

# def add_item(items, item):
#     items.append(item)
#     return items

# print(add_item(["Python", "Java"], "C++"))
# # ["Python", "Java", "C++"]

# print(add_item([1, 2, 3], 4))
# # [1, 2, 3, 4]


# """Task 2"""

# def remove_item(items, item):

#     items.remove(item)
#     return items

# print(remove_item(["Python", "Java", "C++", "Java"], "Java"))
# # ["Python", "C++", "Java"]

# print(remove_item([1, 2, 3, 2], 2))
# # [1, 3, 2]


# """Task 3"""

# def update_item(items, index, new_value):

#     items[index] = new_value
#     return items 
    

# print(update_item(["Python", "Java", "C++"], 1, "Go"))
# # ["Python", "Go", "C++"]

# print(update_item([10, 20, 30], 0, 100))
# # [100, 20, 30]

# print(update_item(["cat", "dog", "bird"], -1, "fish"))
# # ["cat", "dog", "fish"]


# """Task 4"""

# def get_first_three(items):
#     return items[0:3]

# print(get_first_three(["Python", "Java", "C++", "Go"]))
# # ["Python", "Java", "C++"]

# print(get_first_three([10, 20, 30, 40, 50]))
# # [10, 20, 30]


# """Task 5"""

# def find_item(items, target):

#     for i in range(len(items)):
#         if items[i] == target:
#             return i
#     return -1

# print(find_item(["Python", "Java", "C++", "Java"], "Java"))
# # 1

# print(find_item([10, 20, 30, 20], 20))
# # 1

# print(find_item(["cat", "dog", "bird"], "bird"))
# # 2

# print(find_item(["cat", "dog", "bird"], "horse"))


# """Task 6"""

# prog_lang_list = []

# while True:

#     user_input_1 = input("Enter 5 different programming languages one at a time: ")
#     prog_lang_list.append(user_input_1)

#     if len(prog_lang_list) == 5:

#         print(f"Languages: {prog_lang_list}")
#         print(f"Number of languages: {len(prog_lang_list)}")
#         print(f"First language: {prog_lang_list[0]}")
#         print(f"Last language: {prog_lang_list[-1]}")

#         user_input_2 = input("Enter one more programming language: ")
#         prog_lang_list.append(user_input_2)

#         print(f"Updated languages: {prog_lang_list}")

#         break


# """Task 7"""

# user_input = input("Enter your sentence: ")
# user_input_split = user_input.strip().lower().split()

# print(f"Number of words: {len(user_input_split)}")
# print (f"First word: {user_input_split[0]}")
# print (f"Last word: {user_input_split[-1]}")

# if "python" in user_input_split:
#     print(f"'python' appears {user_input_split.count("python")} times")
# else:
#     print("Python wasn't mentioned.")


# """Task 8"""

# shopping_list = []

# for i in range(5):

#     user_input = input("Enter 5 items, one at a time: ")
#     shopping_list.append(user_input)

# print(f"Shopping list: {shopping_list}")

# user_input = input("What item do you want to remove? ")

# if user_input in shopping_list:
#     shopping_list.remove(user_input)
#     print(shopping_list)
# else:
#     print("The item wasn't found.")



