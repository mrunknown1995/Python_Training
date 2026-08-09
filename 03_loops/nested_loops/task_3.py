
"""Task 3"""

students = [
    ["John", "Python", "Git"],
    ["Alex", "Linux", "Docker"],
    ["Maria", "HTML", "CSS"]
]

for inner_list in students:
    print(f'{inner_list[0]}:')

    for i in range(1, len(inner_list)):
        print(inner_list[i])
    print()
