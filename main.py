import random

class Grid:
    def __init__(self, size, bomb):
        self.size = size
        self.width = size
        self.height = size
        self.bombs = bomb
        self.rows = []
        self.getGrid()

    def getGrid(self):
        for row in range(0, self.size):
            row = []
            for count in range(0, self.width):
                row.append(" X ")
            self.rows.append(row)
        return self.rows

    def place_bomb(self):
        for bomb in range(0, self.bombs):
            locationX = random.randint(0, self.size-1)
            locationY = random.randint(0, self.size-1)
            #print(locationY)
            #print(locationX)
            self.rows[0-locationY].pop(locationX)
            self.rows[0-locationY].insert(locationX, " - ")
            #print("Bomb at: ({},{})".format(locationX+1, locationY))

    def updateGrid(self):
        pass

    def __repr__(self):
        rowStr = ""
        for row in self.rows:
            joinedRow = "".join(row)
            rowStr += joinedRow
            rowStr += "\n"
        return rowStr



def print_display_grid(row_list):
    rowStr = ""
    for row in row_list:
        joinedRow = "".join(row)
        rowStr += joinedRow
        rowStr += "\n"
    print(rowStr)


#size_input = input("What size of game?: ")
#bomb_input = input("How many bombs?: ")

size_input = 10
bomb_input = 20

user_grid = Grid(int(size_input),int(bomb_input))
display_grid = []

display_grid = user_grid.rows.copy()

print(display_grid)

print_display_grid(display_grid)

user_grid.place_bomb()

print(display_grid)

print_display_grid(display_grid)


#print(user_grid)
