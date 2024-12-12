#5(i)

class Book:
    def __init__(self,title,author,pages):
        self.author = author
        self.title = title
        self.pages = pages
    def display_info(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")  
        print(f"Pages:{self.pages}")
        
    book =("julian from kagadi","footballer", "256")
    book.display_info()

 #5(ii)

class EBook (Book):
    def __init__(self,title,author,pages,file_size):
        super().__init__(title, author,pages)
        self.file_size = file_size
        
    def display_info(self):
        super().display_info()
        print(f"file_size:{self.file_size}GB")
        
ebook = EBook("julian from kagadi", "footballer", 256, 13)
ebook.display_info()

# Add an additional attribute "format" to the EBook class.
# Display for an instance of the EBook class.

class EBook:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def get_book_info(self):
        return f"Title:{self.title}, Author:{self.author}"
    
class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format
        
    def display_info(self):
        return f"{self.get_book_info()}, Format:{self.format}"
    
if __name__ == "__main__" :  
        ebook = EBook("julian from kagadi", "footballer","PM")
print(ebook.display_info())

#5(iii)
class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def display_info(self):
        print(f"Title:{self.title}, Author:{self.author}") 
book =Book("julian from kagadi", "footballer")
book.display_info()

#5(iv)
#class is a blue print for creating objects and it defines attributes. also methods that an object of a class can have

#Object is an instance of a class
