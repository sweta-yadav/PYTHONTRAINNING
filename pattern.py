b=int(input("enter num of blocks"))
l=int(input("enter num of blocks"))
s=int(input("enter num of blocks"))
for i  in range(b):
    c=0
    for j in range(l-i):
        for k in range(s):
            print("*",end="")
            c=c+1
        print()
        print(c)
        print("_")

