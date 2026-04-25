import json
books = [
    {"title": "The Clean Coder", "author": "Robert Cecil Martin", "year": 2011},
    {"title": "Grokking Algorithms", "author": "Aditya Y. Bhargava", "year": 2016},
    {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017}
]
file = open("books.json", "w")
json.dump(books, file, indent=4)
file.close()