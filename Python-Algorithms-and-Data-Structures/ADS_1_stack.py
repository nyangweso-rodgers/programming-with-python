# Implementation of Stack using Python's list

languages = ['Python', 'JavaScript', 'Java']
languages.append('C#')
languages.append('C++')

print(languages); # Output: ['Python', 'JavaScript', 'Java', 'C#', 'C++']
print(languages.pop()) # Output: C++
print(languages) # Output: ['Python', 'JavaScript', 'Java', 'C#']
print(languages.pop()) # Output: C#
print(languages) # Output: ['Python', 'JavaScript', 'Java']