# for loop

# Example:
## sum numbers in a list
sample_list = [i for i in range(100)]

sum_of_list = 0
for i in sample_list:
    sum_of_list = sum_of_list + i
    
print(sum_of_list)

# Example
## find the sum of negative numbers in a list
second_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
sum_of_second_list  = 0
for i in second_list:
    if i < 0:
        sum_of_second_list += i
        
print(sum_of_second_list)

# Example
## character processing 
## code fragment iterates over a list of strings and for each string process each character by appending it to a list. 
## The result is a list of all letters in all of the words:  
first_names = ['Rodgers', 'Omondi', 'Nyangweso']
letters = []

for n in first_names:
    for l in n:
        letters.append(l)
        
print(letters)

# Example
## asigning scores in a list using a for loop
scores = [19, 89, 45, 23, 90, 27, 30]
scores_grade = []

for score in scores:
    if score >= 90:
        print('A')
        scores_grade.append('A')
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
print(scores_grade)