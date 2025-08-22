a=input("enter boy name:")
b=input("enter girl name:")
a1=list(a)
b1=list(b)
for i in range(len(a1)):
    for j in range(len(b1)):
        if(a1[i]==b1[j]):
            a1[i]==b[j]
            a1[i]='2'
            b1[j]='2'
print(a1)
print(b1)
c=0
for i in a1:
    if(i!='2'):
        c=c+1


