class Book:
    def __init__(self, title: str, author:str):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title+' by '+self.author

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self, title, author):
        b = Book(title, author)
        if b not in self.books:
            self.books.append(b)
        return b

    def get_books(self):
        return self.books

    def get_authors(self):
        return set([b.author for b in self.books])

    def by_author(self,author):

        if author not in self.get_authors():
            raise KeyError('Author '+author+' is not in the library')
        else:



    def __len__(self):
        return len(self.books)



book=Book('Sherlock Holmes', 'Arthur Conan Doyle')
print(book)