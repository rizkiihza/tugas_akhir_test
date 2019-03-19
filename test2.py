
from experiment import Experiment

experiment = Experiment()

class Cell:
    def __init__(self):
        self.char = '_'

    def __str__(self):
        return self.char
    
    def __repr__(self):
        return self.char

class TicTacToe:
    def __init__(self, n, limit):
        self.n = n
        self.limit = limit
        self.board = [[Cell() for _ in range(n)] for _ in range(n)]
        self.current_move = 0

    def move(self, i, j):
        if self.current_move % 2 == 0:
            experiment.flag("current_move%2==0")
            current_char = 'X' 
        else:
            experiment.flag("current_move%2==1")
            current_char = 'O'

        self.board[i][j].char = current_char    
        is_end = self.check(i, j, current_char)

        self.current_move += 1

        if is_end:
            experiment.flag("is_end=True")
            return True, current_char
        else:
            experiment.flag("is_end=False")
            return False, current_char

    def is_valid(self, i, j):
        return i >= 0 and j >= 0 and i < self.n and j < self.n

    def check(self, i, j, current_char):
        # left right
        count1 = self.check_line(i, j, 0, 1, current_char)
        count2 = self.check_line(i, j, 0, -1, current_char)

        count = count1 + count2
        is_horizontal =  count >= self.limit

        if is_horizontal:
            experiment.flag("is_horizontal=True and count=%d" % (count))
        else:
            experiment.flag("is_horizontal=False and count=%d" % (count))

        # up botom
        count1 = self.check_line(i, j, 1, 0, current_char)
        count2 = self.check_line(i, j, -1, 0, current_char)

        count = count1 + count2 - 2
        is_vertical =  count >= self.limit
        if is_vertical:
            experiment.flag("is_vertical=True and count=%d" % (count))
        else:
            experiment.flag("is_vertical=False and count=%d" % (count))

        # top down diagonal
        count1 = self.check_line(i, j, 1, 1, current_char)
        count2 = self.check_line(i, j, -1, -1, current_char)

        count = count1 + count2 - 1
        is_diagonal_top_down =  count >= self.limit
        if is_diagonal_top_down:
            experiment.flag("is_diagonal_top_down=True and count=%d" % (count))
        else:
            experiment.flag("is_diagonal_top_down=False and count=%d" % (count))

        # down top diagonal
        count1 = self.check_line(i, j, -1, 1, current_char)
        count2 = self.check_line(i, j, 1, -1, current_char)

        count = count1 + count2 - 1
        is_diagonal_down_top = count >= self.limit
        if is_diagonal_down_top:
            experiment.flag("is_diagonal_down_top=True and count=%d" % (count))
        else:
            experiment.flag("is_diagonal_down_top=False and count=%d" % (count))
        
        return is_horizontal or is_vertical or is_diagonal_top_down or is_diagonal_down_top

    def check_line(self, i, j, add_i, add_j, current_char):
        count = 0

        c_i, c_j = i, j
        while self.is_valid(c_i, c_j) and self.board[c_i][c_j].char == current_char:
            count += 1
            c_i += add_i
            c_j += add_j

        return count

    def print(self):
        print()
        for row in self.board:
            print(row)
        print()

if __name__ =='__main__':
    label = int(input("label: "))
    experiment.start_experiment(label)

    is_end = False
    tic_tac_toe = TicTacToe(3, 3)
    tic_tac_toe.print()
    while not is_end:
        i, j = list(map(int, input("input cordinate:").split(" ")))

        if i == -1 and j == -1:
            break

        is_end, winner = tic_tac_toe.move(i, j)
        tic_tac_toe.print()
    
    if is_end:
        print("winner is : ", winner)

    experiment.flag("game_end=%s" % ("True" if is_end else "False"))

    experiment.end_experiment()