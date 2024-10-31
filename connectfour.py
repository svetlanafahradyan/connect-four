class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = self.make_new_board()


    def make_new_board(self):
        return [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def display(self):
        print("   ".join(str(i) for i in range(self.columns)))
        print("  " + "----" * self.columns)

        for row in self.board:
            print(" | ".join(['   ' if cell is None else f' {cell} ' for cell in row]))
            print("  " + "----" * self.columns)
    
    def place_disc(self, column, disc_color):
        if self.is_full(column):
            print("Column is full. Choose another column.")
            return False
        
        for row in reversed(range(self.rows)):
            if self.board[row][column] is None:
                self.board[row][column] = disc_color
                return True 
        
        return False
    
    def is_full(self, column):
        return self.board[0][column] is not None
    

    def check_win(self, disc_color):
        return (self.check_horizontal(disc_color) 
                or self.check_vertical(disc_color) 
                or self.check_diagonal(disc_color))
    
    def check_horizontal(self, disc_color):
        for row in self.board:
            count = 0 
            for cell in row:
                count = count + 1 if cell == disc_color else 0
                if count >= 4:
                    return True 
                
        return False
                
    def check_vertical(self, disc_color):
        for column in range(self.columns):
            count = 0 
            for row in range(self.rows):
                count = count + 1 if self.board[row][column] == disc_color else 0
                if count >= 4:
                    return True 
        return False
    
    def check_diagonal(self, disc_color):
        # ascending diagonal check
        for row in range(self.rows - 3):
            for column in range(self.columns - 3):
                if (self.board[row][column] == disc_color and
                    self.board[row + 1][column + 1] == disc_color and
                    self.board[row + 2][column + 2] == disc_color and
                    self.board[row + 3][column + 3] == disc_color):
                    return True 
                
        # descending diagonal check
        for row in range(3, self.rows):
            for column in range(self.columns - 3):
                if (self.board[row][column] == disc_color and
                    self.board[row - 1][column +1] == disc_color and 
                    self.board[row - 2][column + 2] == disc_color and
                    self.board[row - 3][column + 3] == disc_color):
                    return True
                
        return False
    
    def check_draw(self):
        for column in range(self.columns):
            if self.board[0][column] is None:
                return False
        return True


class Player:
    def __init__(self, name, disc_color):
        self.name = name
        self.disc_color = disc_color

class Game:

    def __init__(self):
        self.board = Board()
        self.player_1 = Player("Player 1", "R")
        self.player_2 = Player("Player 2", "Y")
        self.current_player = self.player_1

    def start(self):
        game_over = False 

        while not game_over:
            self.board.display()

            current_player_input = input(f"{self.current_player.name}, choose a column (0-6): ")

            if not current_player_input.isdigit():
                print("Invalid input! Please enter a number between 0 and 6.")
                continue

            current_player_input = int(current_player_input)

            if current_player_input < 0 or current_player_input >= self.board.columns:
                print("Column out of range! Please choos a column between 0 and 6.") 
                continue

            
            if self.board.place_disc(current_player_input, self.current_player.disc_color):
                if self.board.check_win(self.current_player.disc_color):
                    self.board.display()
                    print(f"{self.current_player.name} wins!")
                    game_over = True
                elif self.board.check_draw():
                    self.board.display()
                    print("Try again.")
                    game_over = True
                else:
                    self.current_player = self.player_2 if self.current_player == self.player_1 else self.player_1
            else:
                print("Column is full. Try again.")


game = Game()
game.start()