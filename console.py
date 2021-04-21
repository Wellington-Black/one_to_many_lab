import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


# author_repository.delete_all()
# book_repository.delete_all()

author_1 = Author("Wellington Black")
author_2 = Author("Andrew High")

author_repository.save(author_1)
author_repository.save(author_2)

book_1 = Book("How To Dance", author_1)
book_2 = Book("How To Brew", author_2)

book_repository.save(book_1)
book_repository.save(book_2)

pdb.set_trace()