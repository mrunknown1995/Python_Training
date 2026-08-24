
# """"Task 1"""

# prog_lang_set = set()

# for item in range(5):

#     user_input = input("Enter only_user1 programming language: ")
#     prog_lang_set.add(user_input)

# print(f"Languages: {prog_lang_set}")
# print(f"Number of unique languages: {len(prog_lang_set)}")


# """Task 2"""

# user1_set = set()

# for item in range(3):
#     user1_input = input("Enter only_user1 programming language: ")
#     user1_set.add(user1_input)

# user2_set = set()

# for item in range(3):
#     user2_input = input("Enter only_user1 programming language: ")
#     user2_set.add(user2_input)

# common_langs = user1_set.intersection(user2_set)

# if common_langs:
#     print(f"Common languages: {common_langs}")
# else:
#     print("You have no programming languages in common.")


# """Task 3"""

# tag_set = set()

# for _ in range(6):

#     user_input = input("Enter only_user1 tag: ")
#     tag_set.add(user_input)

# print(f"Unique tags: {tag_set}")
# print(f"Number of unique tags: {len(tag_set)}")

# user_input = input("What tag do you want to check? ")

# if user_input in tag_set:
#     print("Tag found")
# else:
#     print("Tag not found")


# """Mini-Program: Shared Interests"""

# user1_set = set()

# for _ in range(5):
#     user1_input = input("User 1, enter your interest: ")
#     user1_set.add(user1_input)

# user2_set = set()
# print()

# for _ in range(5):
#     user2_input = input("User 2, enter your interest: ")
#     user2_set.add(user2_input)

# print()

# print("User 1 interests:")

# for item in user1_set:
#     print(item)
# print()

# print("User 2 interests:")

# for item in user2_set:
#     print(item)
# print()

# shared_interests = user1_set.intersection(user2_set)

# print(f"Shared interests:")

# if shared_interests:
#     for item in shared_interests:
#         print(item)
# else:
#     print("No shared interests found.")

# print()

# only_user1 = user1_set.difference(user2_set)

# print("Only user 1:")

# if only_user1:
#     for item in only_user1:
#         print(item)
# else:
#     print("No items only for user 1")

# print()

# only_user2 = user2_set.difference(user1_set)

# print("Only user 2:")

# if only_user2:
#     for item in only_user2:
#         print(item)
# else:
#     print("No items only for user 2")






