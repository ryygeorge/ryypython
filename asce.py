l1=[]
while True:
    num=int(input("enter elements"))
    l1.append(num)
    ch=input("continue?")
    if ch!='y':
        break
print(l1)

newlist=[i for i in l1 if i%2==0]
newlist.sort()
print("newlist:",newlist)
