def refined_books(books, keyword):
    refined = filter(lambda book: keyword.lower() in book[1].lower(), books)
    return [book[:2] + book[2:] for book in refined]

def fetch_books(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        books_info = list(map(lambda line: line.strip().split('|'), lines))
        return books_info

def compute_total_prices(books):
    total_prices = list(map(lambda book: (book[0], int(book[3]) * float(book[4])), books))
    return total_prices

def main():
    #EX1
    books_list = fetch_books("books.csv")
    print("exercise 1")
    print(books_list)

    #EX2
    refined_books_list = refined_books(books_list, "python")
    print("exercise 2")
    print(refined_books_list)

    #EX3
    total_prices_list = compute_total_prices(refined_books_list)
    print("exercise 3")
    print(total_prices_list)

if __name__ == "__main__":
    main()