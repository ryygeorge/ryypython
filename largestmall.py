l1=[]
while True:
    num=int(input("enter elements"))
    l1.append(num)
    ch=input("continue?")
    if ch!='y':
        break
print(l1)
largest=max(l1);
smallest=min(l1);

print("largest:",largest)
print("smallest",smallest)
