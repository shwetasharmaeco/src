"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction: it is helpful when user only needs to see relevant parts of the code.
object orientation can help hide all the working which is unnecessary for the user to see and understand
but give essential details.

Encapsulation: it is about wrapping data under one unit ( for example : a class)
it is used for hiding and workings of code and methods.

Polymorphism: it can be explained using example of inheritance. if a sub class inherits attributes
and methods from a parent class then same method can be called in two different classes without
defining method under each class separately.
But it is possible to override parent class method.

2. What is a class?

class is a framework or a base model to define and set various attributes.
Now n number of objects can be made using the same model which will use the same
blue print as class.


3. What is a method?

function which belongs to a class is called a method. It is used to define behavior/functionality of the class.



4. What is an instance in object orientation?

Instance is a unique unit of a class. as an example, if Animal is a class
then class Dog and class Cat are two differemt instances of Animal class.


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attribute is shared by all instances (global scope) whereas instance attribute is unique
   to that partivular instance.

   for example:
       class Animals:
           i will use attribute as walk for all the animals

        but if i have fish as an animal i will define fish as an instance which will 
        override walk as swim.

"""


"""2. Road Class"""


class Road():
    num_lanes = 2
    speed_limit = 25

road1 = Road()
road1.num_lanes = 4
road1.speed_limit = 60

Road2 = Road()

"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

    def update_password(self, cur_password, new_password):
    
        if cur_password == self.password:
            self.password = new_password
        else:
            print("Invalid password")



"""4. Build a Library"""


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author
    
class Library(object):
    def __init__(self):
        self.books = []

    def create_and_add_book (self, title, author):
        book_to_be_added = Book (title,author)
        self.books.append(book_to_be_added)

    def find_books_by_author (self,author):
        author_book =[]
        for book in self.books:
            if book.author == author:
                author_book.append(book)
        return author_book



"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

    def calculate_area(self):
        if self.length == self.width:
            super().calculate_area()
        else:
            print ("Invalid Square")

   

