# Exercise 11.3. Memoize the Ackermann function from Exercise 6.2 and see if memoization
# makes it possible to evaluate the function with bigger arguments. Hint: no. Solution: http:
# // thinkpython2. com/ code/ ackermann_ memo. py .

known_m = {}
known_n = {}
def Acr(m,n):
    if m in known_m and n in known_n:
            return 
    if m == 0:
        return n+1
    if n == 0:
        return Acr(m-1,1)
    return Acr(m-1, Acr(m,n-1))

print(Acr(3, 4))
print(Acr(3, 6))

# output
# python3 assign11.3/question1.py
# 125
# 509