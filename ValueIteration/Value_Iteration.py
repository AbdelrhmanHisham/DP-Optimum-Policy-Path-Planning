

def Action(state, mov):
    return [state[0]+mov[0], state[1]+mov[1]]


def Free_Collision(World, Pos):

    Free = True
    Border_x = len(World)-1
    Border_y = len(World[0]) - 1

# Check x Border
    if (Pos[0] < 0 or Pos[0] > Border_x):
        Free = False
# Check y Border
    if (Pos[1] < 0 or Pos[1] > Border_y):
        Free = False
# Ckeck the node is Free or Not
    if (Free == True):
        if (World[Pos[0]][Pos[1]] == 1):
            Free = False

    return Free


def Not_Visited(visit_list, nxt_state):
    return (visit_list[nxt_state[1]][nxt_state[2]] == 0)




Map_World = [[0, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0]
             ]


goal = [len(Map_World)-1, len(Map_World[0])-1]
# goal = [0 , 4]
init = [0,0]
print(goal)

Value_Matrix = [[99 for row in range(len(Map_World[0]))]for col in range(len(Map_World))]

Optimal_Policy = [[' 'for j in range(len(Map_World[0]))]for i in range(len(Map_World))]

print(Map_World[0])
print(Map_World[1])
print(Map_World[2])
print(Map_World[3])
print(Map_World[4])
print(Map_World[5])




cost = 1


movement = [[-1 ,0], #UP
            [0 ,-1], #LEFT
            [1 , 0],  #DOWN
            [0 , 1] #RIGHT
            ]

movement_sign = ['^' ,'<' ,'V' ,'>']


state = "Construct"

while state == "Construct" :
    state = "Finish"

    for i in range(len(Map_World)):
        for j in range(len(Map_World[0])):
            if goal[0] == i and goal[1] == j:
                if Value_Matrix[i][j] > 0:
                    Value_Matrix[i][j] = 0
                    Optimal_Policy[i][j] = '*'
                    state = "Construct"
        
            elif Map_World[i][j] == 0 :
                for a in range(len(movement)):
                    next_state = Action([i,j],movement[a])                    
                    if (Free_Collision(Map_World , next_state) == True):
                        value = cost + Value_Matrix[next_state[0]][next_state[1]]

                        if value < Value_Matrix[i][j] :
                            Value_Matrix[i][j] = value
                            Optimal_Policy[i][j] = movement_sign[a]
                            state = "Construct"



print("******************")
print(Value_Matrix[0])
print(Value_Matrix[1])
print(Value_Matrix[2])
print(Value_Matrix[3])
print(Value_Matrix[4])
print(Value_Matrix[5])
print("******************")

print("******************")
print(Optimal_Policy[0])
print(Optimal_Policy[1])
print(Optimal_Policy[2])
print(Optimal_Policy[3])
print(Optimal_Policy[4])
print(Optimal_Policy[5])
print("******************")
