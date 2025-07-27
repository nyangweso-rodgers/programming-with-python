# Class Variables vs Instance Variables

# Instance variables
* __Instance variables__ vary from object to object and are declared in the constructor.

# Class variables
* __Class variables__ remain the same between instances of the same class and are declared at the top-level of a class.

# Class vs instance variables – which should I use?
* Generally speaking, stay away from __class variables__. Just like global variables, class variables are usually a _bad idea because they make it hard to keep track of which parts of your program are making data updates_.