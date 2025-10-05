# Object Orineted Programming (OOP) in Python

## Table Of Contents

# Object Oriented Programming

- **OOP** is a way of writing code that relies on the concepts of **classes** and **objects**. **Class** is a blueprint of an **object**. It contains all the details and **methods** of an **object**. Just like a `string`, `integer`, or `float`, a **class** is a custom type that has some special properties.

- An **object** is an instance of a class. An **object** has two **characteristics**:

  - **Attributes**: attribute of an object usually consists of a **name** and a **value**
  - **Behavior**: behavior of an object is its predefined functions

## Methods

- A **method** is a function that is associated with a **class**, and it has access to all the **properties** of the **object**. i.e., **Methods** are **functions** defined inside the body of a **class**, used to determine the behaviors of an object.
- The special `self` value

  - **Methods** are nested within the **class** declaration.
  - **Methods** always take a special parameter as their first argument called `self`. The `self` variable is a reference to the **object** itself, so by using it you can read and update the properties of the object.

- **Methods vs. Functions**
  - A **function is a piece of code that is called by a name**. You can pass it data to operate on via **parameters** and it can optionally return data. All data that is passed to a function is explicitly passed through **parameters**.
  - A **method is a piece of code that is called by a name that is associated with an object**. Methods and functions are similar but have two key differences:
    - A method is implicitly passed the object on which it was called. i.e., you won't see all the inputs in the parameter list
    - A method is able to operate on data that is contained within the class. i.e., you won't see all the outputs in the return statement.

## Constructors

- It's quite rare in the real-world to see a **class** that defines **properties** in the following way:
  ```py
      class Car:
          color = white
  ```
- It's much more practical to use a **constructor**. In Python, a **constructor** is made with the `__init__()` method, and it is automatically called when a new **object** is created. So, with a **constructor** the code would look like this:
  ```py
      class Car:
          def __init__(self, color):
              self.color = color
  ```

## Instance variables

- **Instance variables** vary from object to object and are declared in the constructor.

## Class variables

- **Class variables** remain the same between instances of the same class and are declared at the top-level of a class.
- **Remarks**:
  - Generally speaking, stay away from **class variables**. Just like global variables, class variables are usually a **bad idea because they make it hard to keep track of which parts of your program are making data updates**.

## Instance vs Class vs Static Methods

- **Instance Methods**:

  - Are what you normally write. They access and modify the specific instance of the class. The first argument is always `self`. i.e., functions that are defined inside a class and can only be called from an instance of that class
  - **Why use it:** When your method needs to read or write instance-specific data like user email or username, use this:
  - **Example**(**Instance Method**):

    ```py
        class UserAccount:
            platform = "MySaasPlatform"

            def __init__(self, username, email):
                self.username = username
                self.email = email

            def get_profiles(self):
                return {
                    "username": self.username,
                    "email": self.email,
                    "platform": self.platform
                }
    ```

    - Now we can use it like below:

      ```py
        user = UserAccount("alice", "alice@example.com")
        print(user.get_profile())

        # {'username': 'alice', 'email': 'alice@example.com', 'platform': 'MySaaSPlatform'}
      ```

    - So, what's happening here?
      - `self.username` and `self.email` are tied to that specific user
      - `self.platform` is accessed from the `class-level` but available to all instances

- **Class Methods**

  - **Class methods** get the class as the first argument, usually named `cls`. That means they can create or manipulate the class itself, not just instances.
  - **Why use it**:
    - Alternate constructors like from a string, a dict, a config file etc.
    - Factory patterns
    - Managing class-level behavior or registration
  - **Example** (**Add Class**)

    ```py
        class UserAccount:
            platform = "MySaaSPlatform"

            def __init__(self, username, email):
                self.username = username
                self.email = email

            def get_profile(self):
                return {
                    "username": self.username,
                    "email": self.email,
                    "platform": self.platform
                }

            @classmethod
            def from_dict(cls, data):
                return cls(data["username"], data["email"])
    ```

    - Usage like:
      ```py
        user_data = {"username": "bob", "email": "bob@example.com"}
        user = UserAccount.from_dict(user_data)
      ```
    - Here:
      - `cls` here refers to `UserAccount`, not an object.
      - `cls(...)` creates a new instance. It’s useful if the class name ever changes or is inherited.

- **Static Methods**

  - **Static methods** don’t get `self` or `cls`. They’re just plain functions living inside a class.
  - **Why use it**
    - Utility functions that logically belong to the class
    - When you want organization without inheritance or context
    - Formatting, parsing, validating, etc.
  - **Example** (**Add Static Method**)

    ```py
        class UserAccount:
            platform = "MySaaSPlatform"

            def __init__(self, username, email):
                self.username = username
                self.email = email

            def get_profiles(self):
                return {
                    "username": self.username,
                    "email": self.email,
                    "platform": self.platform
                }
            @classmethod
            def from_dict(cls, data):
                return cls(data["username"], data["email"])

            @staticmethod
            def is_valid_email(email):
                return "@" in email and "." in email
    ```

    - Example Usage:
      ```py
        print(UserAccount.is_valid_email("test@company.com"))
      ```
    - Here:
      - There is no access to `self` or `cls`
      - Think of it as a "related tool" rather than behavior
    - In a real-life example, we can validate data before creating a user which is so useful:

      ```py
        data = {"username": "jane", "email": "janeexample.com"}

        if UserAccount.is_valid_email(data["email"]):
            user = UserAccount.from_dict(data)
        else:
            print("Invalid email format")
      ```

## Inheritance

- In Python, one class can inherit from another using the following syntax:
  ```py
      class Animal():
          # parent animal class
      class Cow(Animal):
          # child class "Cow" inherits "Animal"
  ```

* In order to use the constructor of the parent class, we can use Python's built in **super()** method.

## Encapsulation

## Polymorphism

- **Polymorphism** in programming is the ability to present the same interface (**function** or **method** signatures) for many different underlying forms (data types).
- **Example**:
  - A classic example is a **Shape** class that **Rectangle**, **Circle**, and **Triangle** can inherit from.
  - With **polymorphism**, each of these classes will have different underlying data. The **circle** needs a **center** and **radius**. The **rectangle** needs two co-ordinates for the top left and bottom right corners. The **triangle** needs coordinates for the corners.
  - By making each **class** responsible for its data and its code, you can achieve **polymorphism**.
  - In this example, each class would have its own `__Draw()__` method. This allows the code that uses the different shapes to be simple and easy, and more importantly, it can treat shapes as the same even though they are different. It hides the complexities of the difference behind a clean abstraction.
    ```py
        shapes = [Circle(5, 10), Rectangle(1, 3, 5, 6)]
        for shape in shapes:
            print(shape.Draw())
    ```
  - This is in contrast to the **functional** way of doing things where you would have had separate functions that have different function signatures, like `draw_rectangle(x1, y1, x2, y2)` and `draw_circle(center, radius)`.

# Resources and Further Reading

1. [Object Oriented Programming in Python – Full Crash Course](https://www.freecodecamp.org/news/crash-course-object-oriented-programming-in-python/)
2. [Instance vs Class vs Static Methods in Python](https://hevalhazalkurt.com/blog/instance-vs-class-vs-static-methods-in-python/?ref=dailydev)
