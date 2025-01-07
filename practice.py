from library_system.books import book_files as bk
title = str(input('Enter book title: \n'))
id = int(input('Enetr book id: \n'))
author = str(input('Enter author name: \n'))
year = int(input('Enter year: '))


r = bk.book_info(title, id, author, year)
print(r)
