string1=input('enter the first string')
string2=input('enter the second string')
if(len(string2)==len(string1)):
        if(sorted(string1)== sorted(string2)):
                print("The strings are anagrams.")
        else:
                print("The strings aren't anagrams.")
else:
        print("process not possiable")