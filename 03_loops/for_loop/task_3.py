
"""Task 3"""

numbers = [3, 8, 15, 22, 7, 10]

for num in numbers:
    if num > 10:
        print(num)

numbers = range(1, 11)

for i in numbers:
    print(numbers[-i])

for i in range(10, 0, -1):
    print(i)

for i in range(3):
    for x in range(3):
        print(i, x)

fruits = ["apple", "banana", "orange", "kiwi"]

for i in range(len(fruits)):
    print(i, fruits[i])

