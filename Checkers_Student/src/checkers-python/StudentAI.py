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
        #opponent made a move
        if len(move) != 0:
            #add opponent's move in own board
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1
        
        #get our all possible moves
        #moves: [[Move([(self.row,self.col),(pos_x,pos_y)])]]
        moves = self.board.get_all_possible_moves(self.color)
        # index = randint(0, len(moves)-1)
        # inner_index = randint(0, len(moves[index])-1)

        index = 0
        inner_index = 0
        move = moves[index][inner_index]
        self.board.make_move(move, self.color)
        return move

    def available_moves_and_checker_num_heuristic(self, board, color):
        pass

    def checker_num_heuristic(self, board, color):
        pass

    def optimal_move_iterative(self, iteration, color) -> int:
        optimal_move_index = 0
        board_copied = self.board
        moves = board_copied.get_all_possible_moves(color)
        if iteration == 0:
            for m in moves:
                board_copied.make_move()
        return optimal_move_index
    
    #TODO: filter the lose moves in 2 situations (play 1 and play 2)
    #Check and filter the next moves that will not cause to lose our checkers
    #moves: [[Move([(self.row,self.col),(pos_x,pos_y)])]]
    def filter_lose_move(self,moves):
        current_board = self.board.board
        pass

    #TODO: choose the moves that can capture the opponent's checkers
