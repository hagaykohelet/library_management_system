import csv



def input_nonempty(prompt):
    while True:
        p = input(prompt).strip()
        if p:
            return p
        print("Input cannot be empty.")

def export_to_csv(books, filename):
    with open(filename, "w", encoding= "utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow((["Title", "Author", "ISBN", "Available"]))
        for book in books:
            writer.writerow([book.title, book.author, book.isbn, book.is_available])
