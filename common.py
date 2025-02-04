l1=list(map(int,input("enter list 1:").split()))
l2=list(map(int,input("enter list 2:").split()))

print(l1)
print(l2)

common=[i for i in l1 if i in l2]

print("common elements are:",common)
