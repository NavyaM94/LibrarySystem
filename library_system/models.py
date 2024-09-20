class Book:
    def __init__ (self, title: str, author: str, genre: str, is_borrowed: bool = False):
        self.title = title
        self.author= author
        self.genre= genre
        self.is_borrowed = is_borrowed
        self.duedate=None
    
    def __str__(self):
        return f"title is {self.title}, author is {self.author} and genre is {self.genre}"

class User:
    def __init__(self, name: str):
        self.name=name
        self.borrowed_booklist = []

    def __str__(self):
        return f"name of the candidate is {self.name}, and books borrowed by user are {self.borrowed_booklist}"

