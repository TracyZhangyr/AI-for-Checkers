from random import randint
from BoardClasses import Move
from BoardClasses import Board
# The following part should be completed by students.
# Students can modify anything except the class name and exisiting functions and varibles.

class StudentAI():

    def __init__(self, col, row, p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col, row, p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1: 2, 2: 1}
        self.color = 2

    def get_move(self, move):
        if len(move) != 0:
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        # index = randint(0, len(moves)-1)
        # inner_index = randint(0, len(moves[index])-1)

        index = 0
        inner_index = 0
        move = moves[index][inner_index]
        self.board.make_move(move, self.color)
        return move

    def available_moves_and_checker_num_heuristic(self, board, color):
        if color == 1:
            return board.black_count - board.white_count
        else:
            return board.white_count - board.black_count

    def checker_num_heuristic(self, board, color):
        pass

    '''
    def optimal_move_iterative(self, iteration, color) -> int:
        optimal_move_index = 0
        board_copied = self.board
        moves = board_copied.get_all_possible_moves(color)
        if iteration == 0:
            for m in moves:
                board_copied.make_move()
        return optimal_move_index
    '''

    def optimal_move(self, ):