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
        selected_move = self.optimal_move(moves)
        index = selected_move[0]
        inner_index = selected_move[1]

        move = moves[index][inner_index]
        self.board.make_move(move, self.color)
        return move

    def available_moves_and_checker_num_heuristic(self, board, color):
        pass

    def checker_num_heuristic(self, board, color):
        if color == 1:
            return board.black_count - board.white_count
        else:
            return board.white_count - board.black_count

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


    def opposite_color(self,color):
        return self.opponent[color]

    def optimal_move(self, moves) -> "moves:(int,int)":
        max_heuristic = 0
        result = (0, 0)
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                self.board.make_move(moves[i][j], self.color)
                if self.board.is_win(self.opposite_color(self.color)):
                    self.board.undo()
                    continue
                if self.checker_num_heuristic(self.board, self.color) > max_heuristic:
                    max_heuristic = self.checker_num_heuristic(self.board, self.color)
                    result = (i, j)
                self.board.undo()
        return result

    #TODO: filter the lose moves in 2 situations (play 1 and play 2)
    #Check and filter the next moves that will not cause to lose our checkers
    #*v
    '''
    def filter_lose_move(self,moves):
        current_board = self.board.board
        pass
    '''


