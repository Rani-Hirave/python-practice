# Q2 If you are trying to print a string, what happens if you leave out one of the quotation marks,
# or both?

print('Hello, World!)

# ******************output***************
# File "question2.py", line 4
#     print('Hello, World!)
#                         ^
# SyntaxError: EOL while scanning string literal

print(Hello, World!)

# python3 question2.py
#   File "question2.py", line 4
#     print(Hello, World!)
#                       ^
# SyntaxError: invalid syntax