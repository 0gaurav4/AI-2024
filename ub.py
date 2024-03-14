class ConnectFour:
    def _init_(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)

    def drop_piece(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True
        return False

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        for row in range(6):
            for col in range(7):
                if (col + 3 < 7 and self.board[row][col] == self.current_player and
                        self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3]):
                    return True

                if (row + 3 < 6 and self.board[row][col] == self.current_player and
                        self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col]):
                    return True

                if (row + 3 < 6 and col + 3 < 7 and self.board[row][col] == self.current_player and
                        self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]):
                    return True

                if (row - 3 >= 0 and col + 3 < 7 and self.board[row][col] == self.current_player and
                        self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3]):
                    return True
        return False

    def play(self):
        while True:
            self.print_board()
            column = int(input(f"Player {self.current_player}, enter column (0-6): "))
            if column < 0 or column > 6:
                print("Column out of range. Please choose a column between 0 and 6.")
                continue

            if not self.drop_piece(column):
                print("Column is full. Please choose another column.")
                continue

            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            self.switch_player()

if __name__ == "_main_":
    game = ConnectFour()
    game.play()