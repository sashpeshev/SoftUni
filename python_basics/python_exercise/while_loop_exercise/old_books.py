find_book = input()
book = input()
book_is_find = False
counter = 0
while book != "No More Books":
    if book == find_book:
        book_is_find = True
        break
    counter += 1
    book = input()
if book_is_find:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
