# Exercise 8.1. Read the documentation of the string methods at http: // docs. python. org/ 3/
# library/ stdtypes. html# string-methods . You might want to experiment with some of them
# to make sure you understand how they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing.
# For example, in
# find(sub[, start[, end]]) , the brackets indicate optional arguments. So sub is required, but
# start is optional, and if you include start , then end is optional.

str = 'Python Py'
result = str.find('Py')
print(result)

result = str.find('Py', 1)
print(result)

result = str.find('test')
print(result)

# output
# python3 assign8.1/question1.py
# 0
# 7
# -1