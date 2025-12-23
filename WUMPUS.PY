Empty=''
PIT='P'
WUMPUS='W'
AGENT='A'
GOAL='G'
world=[
    ['','','','P'],
    ['','W','',''],
    ['','','',''],
    ['A','','','G'],
    ]

agent_pos=(3,0)

visited=[[False for _ in range(4)] for _ in range(4)]

moves=[(0,1),(1,0),(0,-1),(-1,0)]

def is_valid(x,y):
    return 0<=x<4 and 0<=y<4

def dfs(x,y):
    if not is_valid(x,y) or visited[x][y]:
        return False
    visited[x][y]=True
    if world[x][y]==PIT or world[x][y]== WUMPUS:
        print(f"agent dies at:({x}{y})!")
        return False
    if world[x][y]==GOAL:
        print(f"gold found:({x}{y})")
        return True
    for dx,dy in moves:
        new_x,new_y=x+dx,y+dy
        if is_valid(new_x,new_y) or not visited[new_x][new_y]:
            if dfs(new_x,new_y):
                print(f"moved to ({new_x},{new_y})")
                return True
    return False
if not dfs(agent_pos[0],agent_pos[1]):
    print("no path found")

