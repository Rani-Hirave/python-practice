# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?

bookprice=24.95
discount=.40
shipingcostfirst=3
shipingaditionalcopy=.70
totalcopy=60

bookDiscountAmount = bookprice * discount * totalcopy
shipping = shipingaditionalcopy * 59 - 1 + shipingcostfirst

totalcost = bookDiscountAmount + shipping

print("totalcost is: " + str(totalcost))