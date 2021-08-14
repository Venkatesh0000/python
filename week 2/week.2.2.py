def fun():
    a= int(input('enter first return value: '))
    b=int(input('enter second return value: '))
    return (a+b,a*b,a-b)
d=fun()
print(d)