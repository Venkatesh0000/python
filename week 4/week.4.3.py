s=input('enter the main string : ')
ss=input('enter the sub string : ')
if ss in s:
    print(ss,'is a substring of ',s)
else:
    print(ss,'is not a substring in ',s)