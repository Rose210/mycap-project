#creating a function called most_frequent
""" Print letters of string in decreasing order of frequency"""

def most_frequent(str):
    str=input("Please enter the string")# asking string from the user
    count = {}

    for x in reversed(str):#counting the elements in the sting
        if x in count.keys():
            count[x]+=1
        else:
            count[x]=1

    for x in count.keys():# print the elrments with its ocurrence
        print (x,"=",count[x])



#str ="mississippi"
most_frequent(str)# calling the function
