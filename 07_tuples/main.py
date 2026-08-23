
# """Task 1"""

# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# user_prog_lang = input("Enter your programming language: ")

# user_info = (user_name, user_age, user_prog_lang)

#   print(f"User: {user_info}")
#   print(f"Name: {user_name}")
#   print(f"Age: {user_age}")
#   print(f"Language: {user_prog_lang}")


# """Task 2"""

# book_title = input("Enter book title: ")
# book_author = input("Enter author: ")
# book_pub_year = input("Enter publication year: ")

# book_tuple = book_title, book_author, book_pub_year

# def book_info(readable_tuple):

#       print("\n--- Book Information ---")
#       print(f"Title: {readable_tuple[0]}")
#       print(f"Author: {readable_tuple[1]}")
#       print(f"Year: {readable_tuple[2]}")

# book_info(book_tuple)


# """Task 3"""

# prog_languages = ("Python", "C++", "C#", "Go", "Kotlin")

# user_input = input("Enter a programming language: ")

# if user_input in prog_languages:
#       print(f"{user_input} is in the list.")
# else:
#       print(f"{user_input} wasn't found.")

#   print(f"First language: {prog_languages[0]}")
#   print(f"Last language: {prog_languages[-1]}")
#   print(f"Number of languages: {len(prog_languages)}")


# """Task 4"""

# movie_info = ("Inception", "Christopher Nolan", "2010")
# title, director, year = movie_info

#   print(f"Movie: {title}")
#   print(f"Director: {director}")
#   print(f"Year: {year}")


# """Mini Book Catalog"""

# books = []

# for i in range(3):

#     book_title = input('Enter book title: ')
#     book_author = input('Enter an author: ')
#     book_year = input('Enter year: ')
    
#     book_info = (book_title, book_author, book_year)
#     books.append(book_info)

# print()
# print("Book catalog:\n")

# for book in books:
#     title, author, year = book

#     print(f"Title: {title}")
#     print(f"Author: {author}")
#     print(f"Year: {year}")
#     print()

# title_check = input('Enter a title to find a book: ')
# found = False

# for tple in books:
#     title, author, year = tple

#     if title_check == title and title_check in tple:

#         print("Book found!")
#         print(f"Title: {title}")
#         print(f"Author: {author}")
#         print(f"Year: {year}")
#         found = True
#         break

# if not found:
#     print("Book isn't found.")
        
 