def nextMove(n,r,c,grid):
    #finds the position of the princess
    for i in range(n):
        princess_position = [i, grid[i].find('p')]
        if princess_position[1] != -1: break
    for k in range(2):
        is_vertical = k == 0
        player_position = r if is_vertical else c
        delta_pos = princess_position[k] - player_position
        if delta_pos < 0:
            return "UP" if is_vertical else "LEFT"
        elif delta_pos > 0:
            return "DOWN" if is_vertical else "RIGHT"
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))