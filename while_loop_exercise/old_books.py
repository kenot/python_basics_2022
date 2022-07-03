# book_name = input()
#
# book_count = 0
# is_book_found = False
#
# current_book = input()
# while current_book != 'No More Books':
#     if current_book == book_name:
#         is_book_found = True
#         print(f'You checked {book_count} books and found it.')
#         break
#
#     book_count += 1
#     current_book = input()
#     if not is_book_found:
#         print(f'The book you search is not here!')
#         print(f'You checked {book_count} books.')

searched_book = input()

books_counter = 0
book_is_found = False

current_book = input()
while current_book != "No More Books":
    if current_book == searched_book:
        book_is_found = True
        break
    books_counter += 1
    current_book = input()
if book_is_found:
    print(f'You checked {books_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_counter} books.')