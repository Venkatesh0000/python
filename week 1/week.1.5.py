ll=int(input('lower limit'))
ul=int(input('upper limit'))
print("Prime numbers between",ll, "and",ul, "are:")
count=0
for num in range(ll,ul+1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           count=count+1
           print(num,end=' ')
print('The total number of prime numbers are:',count)