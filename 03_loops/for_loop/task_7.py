
"""Task 7"""

numbers = [4, 15, 20, 7, 30, 11, 8, 50]
new_list = []

for i in numbers:
    if i % 2 == 0 or i > 10:
        new_list.append(i)

print(new_list)

