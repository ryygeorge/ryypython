l1=[]
while True:
    num=int(input("enter elements"))
    l1.append(num)
    ch=input("continue?")
    if ch!='y':
        break
print(l1)

l1.sort()
print("third largest number is:",l1[2])
