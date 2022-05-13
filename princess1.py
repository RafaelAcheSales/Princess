#!/usr/bin/python
class Actor:
    #finds the postion of the char
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

    #calculates distance from princess to player
    def calculate_distance(self, princess: Actor):
        return [x - y for x, y in zip(princess.position, self.position)]

    #moves the player until it reaches the princess
    def reach_princess(self, princess: Actor):
        distance = self.calculate_distance(princess)
        self.walk_x_axis(distance[1])
        self.walk_y_axis(distance[0])

    #computes Y axis movement
    def walk_y_axis(self, value: int):
        if value < 0:
            for i in range(abs(value)):
                self.move_up() 
        elif value > 0:
            for i in range(abs(value)):
                self.move_down() 

    #computes X axis movement       
    def walk_x_axis(self, value: int):
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


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
