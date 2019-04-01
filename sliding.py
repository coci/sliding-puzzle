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
               self.board[7]==7 and self.board[8]==8 and self.board[9]==" " )
    
    def check_not_empty(self,choose):
        return self.board[choose] == " "
    
    def check_space(self,choose):
        return self.board[choose] == " "
    
    def move(self,tile,direction):
        
        s1 = tile
        
        if s1 == 1:
            if direction == 'r' :
                if self.board[2]== " ":
                    self.board[1],self.board[2] = self.board[2],self.board[1]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'd':
                if self.board[4]== " ":
                    self.board[1],self.board[4] = self.board[4],self.board[1]
                else:
                    print("tile you choose to move on . is not empty")
            else:
                print("wrong move")
                
        if s1 == 2:
            if direction == 'r' :
                if self.board[3]== " ":
                    self.board[2],self.board[3] = self.board[3],self.board[2]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'd':
                if self.board[5]== " ":
                    self.board[2],self.board[5] = self.board[5],self.board[2]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'l':
                if self.board[1]== " ":
                    self.board[2],self.board[1] = self.board[1],self.board[2]
                else:
                    print("tile you choose to move on . is not empty")
            
            else:
                print("wrong move") 
                
        if s1 == 3:
            if direction == 'l' :
                if self.board[2]== " ":
                    self.board[3],self.board[2] = self.board[2],self.board[3]
                else:
                    print("tile you choose to move on . is not empty")
                
            elif direction == 'd':
                if self.board[6]== " ":
                    self.board[3],self.board[6] = self.board[6],self.board[3]
                else:
                    print("tile you choose to move on . is not empty")
            
            else:
                print("wrong move")
                
        if s1 == 4:
            if direction == 'r' : 
                if self.board[5]== " ":
                    self.board[4],self.board[5] = self.board[5],self.board[4]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'd':
                if self.board[7]== " ":
                    self.board[4],self.board[7] = self.board[7],self.board[4]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'u':
                if self.board[1]== " ":
                    self.board[4],self.board[1] = self.board[1],self.board[4]
                else:
                    print("tile you choose to move on . is not empty")
            else:
                print("wrong move")
                
        if s1 == 5:
            if direction == 'r' : 
                if self.board[6]== " ":
                    self.board[5],self.board[6] = self.board[6],self.board[5]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'l':
                if self.board[4]== " ":
                    self.board[5],self.board[4] = self.board[4],self.board[5]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'd':
                if self.board[8]== " ":
                    self.board[5],self.board[8] = self.board[8],self.board[5]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'u':
                if self.board[2]== " ":
                    self.board[5],self.board[2] = self.board[2],self.board[5]
                else:
                    print("tile you choose to move on . is not empty")
            else:
                print("wrong move")
                
                
        if s1 == 6:
            if direction == 'l' : 
                if self.board[5]== " ":
                    self.board[6],self.board[5] = self.board[5],self.board[6]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'd':
                if self.board[9]== " ":
                    self.board[6],self.board[9] = self.board[9],self.board[6]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'u':
                if self.board[3]== " ":
                    self.board[6],self.board[3] = self.board[3],self.board[6]
                else:
                    print("tile you choose to move on . is not empty")
            else:
                print("wrong move")
        
        if s1 == 7:
            if direction == 'r' :
                if self.board[8]== " ":
                    self.board[7],self.board[8] = self.board[8],self.board[7]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'u':
                if self.board[4]== " ":
                    self.board[7],self.board[4] = self.board[4],self.board[7]
                else:
                    print("tile you choose to move on . is not empty")
            else:
            	print("wrong move")
            
        if s1 == 8:
            if direction == 'r' : 
                if self.board[9]== " ":
                    self.board[8],self.board[9] = self.board[9],self.board[8]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'u':
                if self.board[5]== " ":
                    self.board[8],self.board[5] = self.board[5],self.board[8]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'l':
                if self.board[7]== " ":
                    self.board[8],self.board[7] = self.board[7],self.board[8]
                else:
                    print("tile you choose to move on . is not empty")
            else:
            	print("wrong move") 
            
        if s1 == 9:
            if direction == 'l' :
                if self.board[8]== " ":
                    self.board[9],self.board[8] = self.board[8],self.board[9]
                else:
                    print("tile you choose to move on . is not empty")
            elif direction == 'u':
                if self.board[6]== " ":
                    self.board[9],self.board[6] = self.board[6],self.board[9]
                else:
                    print("tile you choose to move on . is not empty")
            else:
            	print("wrong move")
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
        user_tile = int(input("which tile you want to change ? (1-9)"))
        user_direction = input("where you want go that thile ? (r = right , l = left , u = up , d = down)")
        let_game.show_board()
        
        if not let_game.check_space(user_tile):
            let_game.move(user_tile,user_direction)
            let_game.show_board()
            if let_game.check_wining():
                print("wooow , you'r win the game")
                game_on = False
            
            
            