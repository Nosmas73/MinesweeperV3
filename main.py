import random

class Grid:
    def __init__(self, size, bomb):
        self.size = size
        self.bombs = bomb
        self.rows = []
        self.bomb_locations = []
        self.displayGrid()
        self.place_bomb()
        self.game_over = False

    def displayGrid(self):
        for row in range(0, self.size):
            row = []
            for count in range(0, self.size):
                row.append(" X ")
            self.rows.append(row)
        return self.rows

    def place_bomb(self):

        for bomb in range(0, self.bombs):
            locationX = random.randint(0, self.size-1)
            locationY = random.randint(0, self.size-1)

            self.bomb_locations.append([locationX, locationY])



    def select_tile(self, x_location, y_location):
        if ([x_location,y_location]) in self.bomb_locations:
            self.game_over = True


    def __repr__(self):
        rowStr = ""

        count = 1
        for row in self.rows:
            joinedRow = str(count) + "".join(row)
            rowStr = joinedRow + "\n" + rowStr

            count += 1
        print(self.bomb_locations)
        return rowStr


size_input = 10
bomb_input = 5

def game():
    play_game = True
    gameGrid = Grid(int(size_input),int(bomb_input))
    while play_game:
        continue_choice = input("Would you like to play?: ")
        if continue_choice != "quit":
            print("Game Starting")
            print(gameGrid)
            user_choiceX = int(input("X: "))
            user_choiceY = int(input("Y: "))
            gameGrid.select_tile(user_choiceX,user_choiceY)

            if gameGrid.game_over == True:
                print("Game Over")
                play_game = False
            #gameGrid.place_bomb()



        else:
            play_game = False



game()
