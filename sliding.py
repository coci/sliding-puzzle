import random

board_game = ["#",1,2,3,4,5,6,7,8," "]


class Board:
    
    def __init__(self,board):
        self.board = board
    
    def shuffle_board(self):
        random.shuffle(self.board)
        hashtag = self.board.index("#")
        if not hashtag == 0:
            self.board[hashtag],self.board[0] = self.board[0],self.board[hashtag]

    def show_board(self):
        print("    |    |    ")
        print(f"  {self.board[1]} |  {self.board[2]} |  {self.board[3]}")
        print("    |    |")
        print("---- ---- ----")
        print("    |    |    ")
        print(f"  {self.board[4]} |  {self.board[5]} |  {self.board[6]}")
        print("    |    |")
        print("---- ---- ----")
        print("    |    |    ")
        print(f"  {self.board[7]} |  {self.board[8]} |  {self.board[9]}")
        print("    |    |    ")
    
    def check_wining(self):
        return (self.board[1]==1 and self.board[2]==2 and self.board[3]==3 and
               self.board[4]==4 and self.board[5]==5 and self.board[6]==6 and
               self.board[7]==7 and self.board[8]==8 and self.board[9]==" ")
    
    def check_space(self,choose):
        return self.board[choose] == " "
    
    def move(self,tile,direction):
        
        if direction == 'r':
            self.board[tile],self.board[tile+1] = self.board[tile+1],self.board[tile]

        if direction == 'l':
            self.board[tile],self.board[tile-1] = self.board[tile-1],self.board[tile]

        if direction == 'u':
            self.board[tile],self.board[tile-3] = self.board[tile-3],self.board[tile]

        if direction == 'd':
            self.board[tile],self.board[tile+3] = self.board[tile+3],self.board[tile]


def user_choose_tile(user_tile,user_direction):
    
    move = Board(board_game)            
    if user_tile == 1:
        if user_direction == 'r' or user_direction == 'd':
            move.move(user_tile, user_direction)

    if user_tile == 2:
        if user_direction == 'r' or user_direction == 'd' or user_direction == 'l':
            move.move(user_tile, user_direction)

    if user_tile == 3:
        if user_direction == 'l' or user_direction == 'd':
            move.move(user_tile, user_direction)

    if user_tile == 4:
        if user_direction == 'u' or user_direction == 'd' or user_direction == 'r':
            move.move(user_tile, user_direction)

    if user_tile == 5:
        if user_direction == 'u' or user_direction == 'd' or user_direction == 'r' or user_direction == 'l':
            move.move(user_tile, user_direction)

    if user_tile == 6:
        if user_direction == 'u' or user_direction == 'd' or user_direction == 'l':
            move.move(user_tile, user_direction)

    if user_tile == 7:
        if user_direction == 'u' or user_direction == 'r':
            move.move(user_tile, user_direction)

    if user_tile == 8:
        if user_direction == 'u' or user_direction == 'l' or user_direction == 'r':
            move.move(user_tile, user_direction)

    if user_tile == 9:
        if user_direction == 'u' or user_direction == 'l':
            move.move(user_tile, user_direction)




print('Welcome to sliding puzzle ')
while True:
    let_game = Board(board_game)
    let_game.shuffle_board()
    let_game.show_board()
    
    userinput = input("are you ready ?(y/n)")
    
    if userinput == 'y':
        game_on = True
    elif userinput == 'n':
        game_on = False
    else :
        print("please print true format (y = yes , n = no)")
        
    
    while game_on:
        
        while True:
            try:
                user_tile = int(input("which tile you want to change ? (1-9)"))

                user_direction = input("where you want go that thile ? (r = right , l = left , u = up , d = down)")
                if user_direction == "q":
                	break
                break
            except:
                continue
        user_choose_tile(user_tile, user_direction)
        let_game.show_board()
        
        if not let_game.check_space(user_tile):
            let_game.move(user_tile,user_direction)
            let_game.show_board()
            if let_game.check_wining():
                print("wooow , you'r win the game")
                game_on = False
            
            
            