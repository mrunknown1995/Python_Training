
# """Task 1"""

# def analyze_text(text):

#     return text.lower(), len(text), text[0]

# print(analyze_text("Python"))
# print(analyze_text("PYTHON"))
# print(analyze_text("ChatGPT"))


# """Task 2"""

# def get_last_three(text):
#     return text[-3:]
        
# print(get_last_three("Python"))
# # "hon"

# print(get_last_three("ChatGPT"))
# # "GPT"


# """Task 3"""

# def first_and_last(text):
#     return text[0], text[-1]

# print(first_and_last("Python"))
# # ("P", "n")

# print(first_and_last("ChatGPT"))
# # ("C", "T")

# print(first_and_last("hello"))
# # ("h", "o")


# """Task 4"""

# def reverse_text(text):
#     return text[::-1]

# print(reverse_text("Python"))
# # "nohtyP"

# print(reverse_text("ChatGPT"))
# # "TPGtahC"


# """Task 5"""

# def clean_text(text):
#     return text.lstrip().rstrip().lower()
    
# print(clean_text("  Python  "))
# # "python"

# print(clean_text("  HELLO WORLD  "))
# # "hello world"

# print(clean_text("   ChatGPT"))
# # "chatgpt"