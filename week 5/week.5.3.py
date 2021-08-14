list1=[]
n=int(input('enter the number of elements you need in the list'))
for i in range(0,n):
    element=int(input('enter each list element'))
    list1.append(element)
even_nos=[num for num in list1 if num%2==0]
print("even numbers in the list:",even_nos)