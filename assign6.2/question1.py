# Exercise 6.2. The Ackermann function, A ( m, n ) , is defined:
# 
# 
#  n + 1
# A ( m, n ) = A ( m − 1, 1 )
# 
# 
# A ( m − 1, A ( m, n − 1 ))
# if m = 0
# if m > 0 and n = 0
# if m > 0 and n > 0.
# See http: // en. wikipedia. org/ wiki/ Ackermann_ function . Write a function named ack
# that evaluates the Ackermann function. Use your function to evaluate ack(3, 4) , which should be
# 125. What happens for larger values of m and n ? Solution: http: // thinkpython2. com/ code/
# ackermann. py

def Ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return Ackermann(m - 1, 1)
    return Ackermann(m-1, Ackermann(m, n - 1))
 
print(Ackermann(3, 4))

# output
# python3 assign6.2/question1.py
# 125