n=int(input('enter the number of rows'))
for i in range (0,n) :
    for j in range (0,n):
        if (i>=j):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()