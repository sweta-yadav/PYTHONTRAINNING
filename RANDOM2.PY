mem=[]
while(len(mem)!=5):
    a=int(input("enter a number:"))
    if a in mem:
        print("this number alreay exist!")
    else:
        mem.append(a)
print(mem)