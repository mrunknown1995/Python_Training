
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