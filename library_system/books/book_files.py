# add books to the library
# books details
book_store = []


def book_info(title, id, author, year):
    book_store.append({
        'id': id,
        'title': title,
        'author': author,
        'year': year
    })
    return f"""
    Book Details:
    Title: {title}
    Id: {id}
    Author: {author}
    Year: {year}
    """
