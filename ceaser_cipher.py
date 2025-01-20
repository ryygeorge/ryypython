t=input("enter the string : ")
distance=int(input("enter the distance "))
encrypt=""
for ch in t:
    ordinalvalue=ord(ch)
    codevalue=ordinalvalue+distance
    if codevalue > ord('z'):
        codevalue=ord('a')+distance-(ord('z')-ordinalvalue+1)
    encrypt=encrypt+chr(codevalue)
print(encrypt)
t=input("enter the string : ")
distance=int(input("enter the distance "))
decrypt=""
for ch in t:
    ordinalvalue=ord(ch)
    codevalue=ordinalvalue-distance
    if codevalue < ord('a'):
        codevalue=ord('z')-(distance-(ord('a')-ordinalvalue-1))
    decrypt=decrypt+chr(codevalue)
print(decrypt)
