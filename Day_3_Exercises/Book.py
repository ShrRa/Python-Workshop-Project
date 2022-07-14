class Book:
    def __init__(self, title: str, author:str):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title+' by '+self.author

book=Book('Sherlock Holmes', 'Arthur Conan Doyle')
print(book)