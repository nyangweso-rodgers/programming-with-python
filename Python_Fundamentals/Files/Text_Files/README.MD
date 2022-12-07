# Text Files

## Table Of Contents

# Openning Files
* Python can be used to __read__ and __write__ the contents of files. Text files are easiest to manipulate. Before a file can be edited, it must be opened, using the __open__ function.
    ```py
        my_file = open("filename.txt")
    ```
* The argument of the open function is the path to the file. If the file is in the current working directory, you can specify only its name.

* __close__ method is used to close a file once a file is opened and used.

# Modes of openning files:
* __r__ - read mode (default)
* __w__ - write mode (rewritting the contents of the file): 
    - The __'w'__ mode will create the file if it doesn't exists already. 
    - When a file is opened in write mode, the file's existing content is deleted. 
    - The write method returns the number of bytes written to a file, if successful.
    - To write something other than a string, it needs to be converted to a string first
* __b__ - append mode (adding new content to the end of the file)
* __'b'__ - binary mode (opens the file in a __binary__ mode (used for non-text files e.g., _image_ and _sound files_)
* __rb__ - binary read mode
* __wb__ - binary write mode

# Remarks
* _Just like passing no arguments, negative values will return the entire contents._

* _After all contents in a file have been read, any attempt to read further from that file will return an empty string - because you are trying to read from the end of the file._

* _To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file._

* _It's a good practice to avoid wating resources by making sure that files are always closed after they have been used. One way of doing this is to use __try__ and __finally___

* _An alternative way of doing this is using __with__ statement. _This creates a temporary variable, which is only accessible in the indented block of the with statement_.

* _We can set the mode to __append__ using a lowercase "a". This will not create a new file but just use the existing file. If we call the method write, it will just write to the existing file then add_