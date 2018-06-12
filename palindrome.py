num1 = int(input())
 
num2 = num1
num3 = 0
 
while num2 != 0:
    num3 = (num3 * 10) + (num2 % 10)
    num2 = num2 // 10
 
if num1 == num3:
    print("yes")
else:
    print("no")
