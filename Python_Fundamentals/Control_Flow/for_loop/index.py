# for loops

# Example 1: summing numbers in a list using a for loop
sample_list = [i for i in range(100)]

sum_of_list = 0
for i in sample_list:
    sum_of_list += i
print(sum_of_list)

# Example 2: find the sum of negative numbers in a list
sample_list2 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0
for i in sample_list2:
    if i < 0:
        total += i
print(total)

# Example 3: character processing using a for loop
word_list = ['Rodgers', 'Omondi', 'Nyangweso']
letter_list = []
for word in word_list:
    for letter in word:
        letter_list.append(letter)
print(letter_list); 
# The above code fragment iterates over a list of strings and for each string process each character by appending it to a list. 
# The result is a list of all letters in all of the words:  

# Example 4: asigning scores in a list using a for loop
scores = [19, 89, 45, 23, 90, 27, 30]

for score in scores:
    if score >= 90:
        print('A')
    else:
        if score >= 80:
            print('B')
        else:
            if score >= 70:
                print('C')
            else:
                if score >= 60:
                    print('D')
                else:
                    print('F')