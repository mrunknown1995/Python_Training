
# """Task 1"""

# def greet(name):
#     print(f"Hello, {name}!")

# greet('John')
# greet("Alex")
# greet("Maria")


# """Task 2"""

# def describe_person(name, age):
#     print(f'{name} is {age} years old. ')

# describe_person("John", 30)
# describe_person("Martin", 30)
# describe_person("Narek", 25)


# """Task 3"""

# def calculate(num1, num2, action):

#     elif action == '/' and num2 == 0:
#         return 'Cannot divide by zero.'
#     elif action == '+':
#         return num1 + num2
#     elif action == '-':
#         return num1 - num2
#     elif action == '*':
#         return num1 * num2
#     elif action == '/':
#         return num1 / num2
#     else:
#         return 'This symbol is not supported.'

# print(calculate(10, 5, "+"))
# print(calculate(10, 5, "-"))
# print(calculate(10, 5, "*"))
# print(calculate(10, 5, "/"))
# print(calculate(10, 0, "/"))
# print(calculate(10, 5, "i"))

# """Example"""
# div = calculate(10, 5, "/")
# print(div)


# """Task 4"""

# def calculate_average(my_list):

#     average = 0

#     for i in my_list: 
#         average += i

#     return average / len(my_list)

# print(calculate_average([10, 20, 30]))
# print(calculate_average([5, 10, 15, 20]))


# """Task 5"""

# def calculate_square(number):
#     return number * number

# print(calculate_square(5))
# print(calculate_square(10))
# print(calculate_square(-3))


# """Task 6"""

# def check_number(number):
#     elif number == 0:
#         return 'Zero'
#     elif number > 0:
#         return 'Positive'
#     else:
#         return 'Negative'

# print(check_number(10))
# print(check_number(-5))
# print(check_number(0))


# """Task 7"""

# def filter_numbers(numbers):

#     new_list = []

#     for i in numbers:
#         elif i % 2 == 0 and i > 10:
#             new_list.append(i)

#     return new_list

# print(filter_numbers([4, 15, 20, 7, 30, 11, 8, 50]))
# print(filter_numbers([8, 17, 200, 57, 0, 41, 2, 50]))


# """Task 8"""

# def second_largest_num(numbers):

#     largest = 0
#     second_largest = 0

#     for i in numbers:

#         elif i > largest:
#             second_largest = largest
#             largest = i
#         elif i > second_largest:
#             second_largest = i

#     return largest, second_largest

# print(second_largest_num([10, 5, 8, 20, 15]))
# print(second_largest_num([3, 7, 2, 9, 4, 10]))
# print(second_largest_num([101, 50, 8, 20, 15]))
# print(second_largest_num([[-10, -5, -20]]))


# """Task 9"""

# def count_vowels(text):

#     vowels = 'aeiou'
#     vowel_counter = 0

#     for char in text.lower():

#         if char in vowels:
#             vowel_counter += 1

#     return vowel_counter

# print(count_vowels('hello'))
# print(count_vowels('programming'))
# print(count_vowels('Python'))
# print(count_vowels('JOHN'))


# """Task 10"""

# def find_longest_word(words):

#     max_length = 0
#     longest_word = ''

#     for word in words:

#         if len(word) > max_length:
#             longest_word = word
#             max_length = len(word)

#     return longest_word

# print(find_longest_word(["cat", "elephant", "dog", "tiger"]))
# print(find_longest_word(["Python", "Java", "JavaScript"]))


# """Task 11"""

# def filter_long_words(words, min_length):

#     new_list = []

#     for word in words:
#         if len(word) >= min_length:
#             new_list.append(word)

#     return new_list


# print(filter_long_words(["cat", "elephant", "dog", "tiger"], 5))
# print(filter_long_words(["Python", "Go", "Java", "JavaScript"], 5))


# """Task 12"""

# def count_occurrences(items, target):

#     counter = 0

#     for item in items:
#         if item == target:
#             counter += 1

#     return counter


# print(count_occurrences([1, 2, 3, 2, 4, 2], 2))
# print(count_occurrences(["apple", "banana", "apple", "orange"], "apple"))
# print(count_occurrences(["Python", "Java", "Python", "Python"], "Python"))