Write a program to calculate the length of a string without
using the strlen() function.


def lengthOfString(string):
    cnt = 0
    for i in string:
        cnt +=1
    return cnt # 7
string = input() #shubham 
print(lengthOfString(string))
