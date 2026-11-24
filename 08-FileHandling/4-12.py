import csv

def format_book(book):
    return f"{book['Title']},{book['Author']},{book['Year']}\n"

def format_genre(genre):
    return f"books_{genre.lower().replace(" ", "_")}.txt"

def group_books(books):
    genres = {}

    for book in books:
        genre = book["Genre"]
        if genre not in genres:
            genres[genre] = []
        
        genres[genre].append(book)

    return genres

with open("books.csv") as file:
    reader = csv.DictReader(file)
    genres = group_books([book for book in reader])

    for genre, books in genres.items():
        with open(format_genre(genre), "w") as g:
            g.writelines(
                ["Title,Author,Year\n"] +
                [format_book(book) for book in books]
                )