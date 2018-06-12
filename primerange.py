lower11 = int(input("Enter lower range: "))  
upper11 = int(input("Enter upper range: "))  
  
for num11 in range(lower11,upper11 + 1):  
   if num11 > 1:  
       for i in range(2,num11):  
           if (num11 % i) == 0:  
               break  
       else:  
           print(num11)  
