sum=0
ll=int(input('lower limit'))
ul=int(input('upper limit'))
for i in range(ll,ul+1):
    if (i%2==0):
        sum=sum+i
print(sum)