stu=["raj","sweta","sujata","mamata","nikesh"]
marks=[[20,30,70],[80,44,55],[36,78,98],[37,76,54],[44,55,70]]
per=[]
for i in marks:
    d=sum(i)//3
    per.append(d)
for i in range(5):
    print("{}.{}:{}%".format(i+1,stu[i],per[i]))