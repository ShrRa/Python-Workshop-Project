class Book:
    def __init__(self, title: str, author:str):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title+' by '+self.author

    def __eq__(self, other):
        return self.title == other.title and self.author==other.author


class Library:
    def __init__(self, books = None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, title, author):
        b = Book(title, author)
        if b not in self.books:
            self.books.append(b)
        else:
            raise KeyError('The book ' + title+ ' by '+ author+' is already in the library')
        return b

    def get_books(self):
        return self.books

    def get_authors(self):
        return set([b.author for b in self.books])

    def by_author(self,author):
        books=[]
        if author not in self.get_authors():
            raise KeyError('Author '+author+' is not in the library')
        else:
            books = [b for b in self.get_books() if b.author==author]
        return books

    def union(self, other):
        un = self.get_books()
        un2 = [b for b in other.get_books() if b not in un]
        return Library(un+un2)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, item):
        return self.get_books()[item]

    @property
    def titles(self):
        return [b.title for b in self.get_books()]

    @property
    def authors(self):
        return [b.author for b in self.get_books()]

library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')

for book in books:
    print(book)

# books = library.by_author('Carol')

print(library.titles)
print(library.authors)

lib2=Library()
print(lib2.titles)
lib2.add_book('Sherlock Holmes', 'Arthur C. Doyle')
lib2.add_book('HPMR','E. Yudkowsky')
print(lib2.titles)
lib2.add_book('A Different Book', 'Bob')
print(lib2.titles)

print(library.union(lib2).titles)
