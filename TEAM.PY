import random

no = int(input("Enter num of teams: "))
teams = []
matches = []


for i in range(no):
    d = input("Enter team name: ")
    teams.append(d)

meet = int(input("Enter no of meet between same teams: "))


for i in range(no - 1):
    for j in range(i + 1, no):
        for k in range(meet):
            matches.append([teams[i], teams[j]])

random.shuffle(matches)


for i in range(len(matches)):
    print("Match {}. {} Vs {}".format(i + 1, matches[i][0], matches[i][1]))