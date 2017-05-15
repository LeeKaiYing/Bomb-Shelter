class SKObjects:
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.character = character
    def print (self, x, y):
        if self.x == x and self.y == y:
            print(self.character, end="")
            return True
        else:
            return False
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def calculate_next(self, dx, dy):
        nextx = self.x + dx
        nexty = self.y + dy
        return (nextx, nexty)


class Map:
    def __init__(self):#constructor
        self.width = 5
        self.height = 7
        self.chaien = SKObjects(2, 3, " C ")
        self.box = SKObjects (1, 4, " B ")
        self.gate = SKObjects (2, 5, " G ")
        self.objects = [self.chaien, self.box, self.gate]

    def print_objects(self, x, y):
        for object in self.objects:
            if object.print(x, y):
                return True
        return False

    def print(self):
        for y in range (self.height):
            for x in range (self.width):
                if self.print_objects(x, y):
                    pass
                else:
                    print(" - ", end="")
            print()
    def process_input(self):
        move = input("Your Move ?").upper()
        dx = 0
        dy = 0

        if move == "D":
            dx = 1
        elif move == "A":
            dx = -1
        elif move == "W":
            dy = -1
        elif move == "S":
            dy = 1
        [next_x, next_y] = self.chaien.calculate_next(dx, dy)
        self.chaien.x = next_x
        self.chaien.y = next_y





sokoban = Map()
while True:
    sokoban.print()
    sokoban.process_input()