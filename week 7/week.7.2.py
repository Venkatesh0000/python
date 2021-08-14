def intersection_of_two_string(str1,str2):
    result=""
    for ch in str1:
        if ch in str2 and not ch in result:
            result+=ch
    return result
str1=("python3")
str2=("python2.7")
