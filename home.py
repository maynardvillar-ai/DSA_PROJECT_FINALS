import json

# Open and read JSON file
with open("KJV.json", "r") as file:
    data = json.load(file)  # load JSON into Python object

books = []

for i, book in enumerate(data["books"], start=1):
    books.append(book['name'])
    print(f"Book {i}: {book['name']}")


choice = input("\nEnter a number between 1 and 66: ")

if choice.isdigit():
    choice =int(choice)
    if 1 <= choice <= 66:
        print(f"The book for number {choice} is '{books[choice - 1]}'")
else:
    print("Invalid number! Please choose between 1 and 66.")