# print a list which contains 5 randomly gen number(1 to 10)without duplication
import random

# random_numbers = random.sample(range(1, 11), 5)
# print(random_numbers)


l=[]
while(len(l)!=5):
    d=random.randint(1,10)
    if(d not in l):
        l.append(d)
print(l)