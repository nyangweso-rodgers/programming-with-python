## Shortening any link
import pyshorteners

# check methods
# print(dir(pyshorteners))

link = input("Please enter a link: ")
shortner = pyshorteners.Shortener()
x = shortner.tinyurl.short(link)
print(x)