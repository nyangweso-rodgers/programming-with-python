# Implementation of Stack using Python's list

languages = ['Python', 'JavaScript', 'Java']

print(languages); # Output: ['Python', 'JavaScript', 'Java', 'C#', 'C++']
languages.append('C#')

print(languages.pop()) # Output: C++
print(languages) # Output: ['Python', 'JavaScript', 'Java', 'C#']

languages.append('C++')

print(languages.pop()) # Output: C#
print(languages) # Output: ['Python', 'JavaScript', 'Java']