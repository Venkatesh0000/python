a=input('First number')
b=input('Second number')
c=input('Third number')
d=0
if a>=b:
    d=a
    if d>=c:
        print('largest element among three Numbers =',d)
    else:
        print('largest element among three Numbers =',c)
elif b>a:
    d=b
    if d >= c:
        print('largest element among three Numbers =',d)
    else:
        print('largest element among three Numbers =',c)
