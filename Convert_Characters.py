def character(str1):
    upp=0
    low=0
    for i in str1:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upp+=1
        if i in "abcdefghijklmnopqrstuvwxyz":
            low+=1
    if(low<upp):
        newstr=str1.upper()
    elif(low==upp):
        newstr=str1
    else:
        newstr=str1.lower()
    return(newstr)

string1=input("enter a string: ")
result=character(string1)
print(result)
