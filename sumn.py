num10 = int(input())
if num10 < 0:
   print("error")
else:
   sum10 = 0
   while(num10 > 0):
       sum10 += num10
       num10 -= 1
   print(sum10)
