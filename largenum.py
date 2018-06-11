a11 = int(input())
b12 = int(input())
c13 = int(input())
if (a11 >= b12) and (a11 >= c13):
   largest = a11
elif (b12 >= a11) and (b12 >= c13):
   largest = b12
else:
   largest = c13
 
print(largest)
