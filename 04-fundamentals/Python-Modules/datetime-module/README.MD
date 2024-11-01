# datetime Module

## Table Of Contents
- [Further Reading]()
    - [Python datetime](https://www.programiz.com/python-programming/datetime)

* __datetime__ is a module that provides classes for working with dates, times, and time intervals.

# Attributes of datetime Module
* We can use the dir() function to get a list containing all attributes of a module.

    ```py
        import datetime
        print(dir(datetime))
    ```

# Import Only date Class
```py
    from datetime import date

    d = date(2022, 12, 25)
    print(d)
```