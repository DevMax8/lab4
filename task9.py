import json
file = open("books.json", "r")
books = json.load(file)
for book in books:
    if book["year"] > 2015:
        print(book)
file.close()

