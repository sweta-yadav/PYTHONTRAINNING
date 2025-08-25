# student={
    
# }


# for i in student:
#     tot=sum(i["marks"])
#     d=tot//3
#     i["per"]=d

# res=sorted(students,key=lambda x:x["per"],reverse=true)
# des=["FIRST","SECOND","THIRD","FOURTH","FIFTH"]
# for i in range(5):
#     print("RANK {}: mr/ms {}")



students = [
    {"name": "Alice", "marks": [85, 90, 88]},
    {"name": "Bob", "marks": [78, 82, 80]},
    {"name": "Charlie", "marks": [92, 87, 95]},
    {"name": "David", "marks": [70, 75, 72]},
    {"name": "Eve", "marks": [88, 84, 86]},
    {"name": "Frank", "marks": [65, 60, 68]}
]


for i in students:
    tot = sum(i["marks"])
    d = tot / 3  
    i["per"] = d


res = sorted(students, key=lambda x: x["per"], reverse=True)


des = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]


for i in range(5):
    print("RANK {} : Mr/Ms {} has scored {} stands {}"
          .format(i+1, res[i]["name"], res[i]["per"], des[i]))