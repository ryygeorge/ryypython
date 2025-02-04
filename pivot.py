l1=[]
while True:
    num=int(input("enter elements"))
    l1.append(num)
    ch=input("continue?")
    if ch!='y':
        break
print(l1)
pivot=int(input("enter pivot"))
newlist=[i for i in l1 if i<pivot]
print("newlist:",newlist)
