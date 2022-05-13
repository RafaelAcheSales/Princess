#!/usr/bin/python
class Actor:
    def find_char_update_position(self):
        for i in range(self.n):
            self.position = [i, grid[i].find(self.c)]
            if self.position[1] != -1: break
    def __init__(self, n: int, c: str):
        self.n = n
        self.c = c
        self.find_char_update_position()

    
    

class Player(Actor):
    #movement functions
    def move_left(self):
        print("LEFT")
        self.position[1] -= 1
    def move_right(self):
        print("RIGHT")
        self.position[1] += 1
    def move_up(self):
        print("UP")
        self.position[0] -= 1
    def move_down(self):
        print("DOWN")
        self.position[0] += 1
    
    def calculate_distance(self, princess: Actor):
        return [x - y for x, y in zip(princess.position, self.position)]

    def reach_princess(self, princess: Actor):
        distance = self.calculate_distance(princess)
        self.walkXaxis(distance[1])
        self.walkYaxis(distance[0])
        
    def walkYaxis(self, value: int):
        if value < 0:
            for i in range(abs(value)):
                self.move_up() 
        elif value > 0:
            for i in range(abs(value)):
                self.move_down() 
                
    def walkXaxis(self, value: int):
        if value < 0:
            for i in range(abs(value)):
                self.move_left() 
        elif value > 0:
            for i in range(abs(value)):
                self.move_right()
    


def displayPathtoPrincess(n,grid):
    player = Player(n, 'm')
    princess = Actor(n, 'p')
    player.reach_princess(princess)
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
