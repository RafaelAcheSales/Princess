#!/usr/bin/python
PRINCESS_CHAR = 'p'

def displayPathtoPrincess(n,grid):
    #finds the position of the princess
    for i in range(n):
        princess_position = [i, grid[i].find(PRINCESS_CHAR)]
        if princess_position[1] != -1: break
    player_position = [int((n-1)/2), int((n-1)/2)]
    #for each dimension
    for k in range(2):
        #for each cell
        for i in range(n):
            #calculates position variation and moves player
            delta_pos = princess_position[k] - player_position[k]
            is_vertical = k == 0
            if delta_pos < 0:
                move = "UP" if is_vertical else "LEFT"
                print(move)
                player_position[k] -= 1
            elif delta_pos > 0:
                move = "DOWN" if is_vertical else "RIGHT"
                print(move)
                player_position[k] += 1
            

#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)