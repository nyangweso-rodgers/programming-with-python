# Text filees

# reading contents of the file
file_1 = open('test_file_1.txt', 'r')
print(file_1.read())
file_1.close()

# reading each line
file_1 = open('test_file_1.txt', 'r')
print(file_1.readlines())
file_1.close()

# file data type
file_1 = open('test_file_1.txt', 'r')
print(type(file_1))
file_1.close()

# using for loop to iterate through the lines of the files
file_1 = open('test_file_1.txt', 'r')
for line in file_1:
    print(line)
file_1.close()

# writing files using 'w'
file_2 = open('test_file_2.txt', 'w')
file_2.write('// This line has been written to this file. It did not exists before')
file_2.close()

# Alternatively,
my_message = "This is a sample text message"
file_3 = open('test_file_3.txt', 'w')
amount_written = file_3.write(my_message)
print(amount_written)
file_3.close()

# using try and finally methods
try:
    file_1 = open("test_file_1.txt", 'r')
    # read first 2 letters
    print(file_1.read(2))
finally:
    file_1.close()
    
# using with statement
with open('test_file_1.txt', 'r') as file_1:
     # The file is automatically closed at the end of the with statement, even if exceptions occur with it.
     print(file_1.read())
             
# using append method
with open('test_file_4.txt', 'a') as file_4:
    file_4.write("// Using append method to add additional content to the existing file")
    print(file_4)
    
with open('test_file_4.txt', 'r') as file_4:
    for line in file_4:
        print(line)