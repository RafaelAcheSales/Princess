#!/usr/bin/python
class Actor:
    #finds the postion of the char
    def find_char_update_position(self):
        for i in range(self.n):
            self.position = [i, self.grid[i].find(self.c)]
            if self.position[1] != -1: break
    def __init__(self, n: int, c: str, grid: list):
        self.n = n
        self.c = c
        self.grid = grid
        self.find_char_update_position()


class MoveCalculator:
    def __init__(self, princess: Actor):
        self.princess = princess
    def calculate_next_move(self, n, r, c):
        distance = self.calculate_distance(r, c)
        return self.move(distance)
    def calculate_distance(self, r, c):
        return [r - self.princess.position[0], c - self.princess.position[1]]
    def move(self, distance):
        if distance[0] > 0:
            return("UP")
        elif distance[0] < 0:
            return("DOWN")
        elif distance[1] > 0:
            return("LEFT")
        elif distance[1] < 0:
            return("RIGHT")
        return ""
        
    
def nextMove(n,r,c,grid, move_calculator: MoveCalculator):
    return move_calculator.calculate_next_move(n, r, c)

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())
princess = Actor(n, 'p', grid)
move_calculator = MoveCalculator(princess)
print(nextMove(n,r,c,grid, move_calculator))
