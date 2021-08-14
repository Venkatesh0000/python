int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))
print('before swaping')
print(int1,int2)
int1 = int1 + int2
int2 = int1 - int2
int1 = int1 - int2
print('after swaping')
print(int1,int2)