# Ploymorphism in Python

* __Polymorphism__ in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).


# Classic Example
* A classic example is a __Shape__ class that __Rectangle__, __Circle__, and __Triangle__ can inherit from.

* With polymorphism, each of these classes will have different underlying data. The circle needs a center and radius. The rectangle needs two co-ordinates for the top left and bottom right corners. The triangle needs coordinates for the corners.

* By making each class responsible for its data and its code, you can achieve polymorphism.

* In this example, each class would have its own __Draw()__ method. This allows the code that uses the different shapes to be simple and easy, and more importantly, it can treat shapes as the same even though they are different. It hides the complexities of the difference behind a clean abstraction.

    ```py
        shapes = [Circle(5, 10), Rectangle(1, 3, 5, 6)]
        for shape in shapes:
            print(shape.Draw())
    ```

* This is in contrast to the functional way of doing things where you would have had separate functions that have different function signatures, like draw_rectangle(x1, y1, x2, y2) and draw_circle(center, radius).