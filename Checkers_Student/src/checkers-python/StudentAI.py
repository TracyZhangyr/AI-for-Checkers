from random import randint
from BoardClasses import Move
from BoardClasses import Board
import time
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
        self.time = 480

    def get_move(self, move):
        #opponent made a move
        #start = time.time()
        if len(move) != 0:
            #add opponent's move in own board
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1

        #moves: [[Move([(self.row,self.col),(pos_x,pos_y)])]]
        #move = self.minimax(self.board,self.color,4)
        move = self.alpha_beta_search(self.board, self.color, 4)

        self.board.make_move(move, self.color)

        #time_elapsed = time.time() - start
        #self.time = self.time - time_elapsed
        return move

    def count_kings(self, board, color):
        result = 0
        if color == 1:
            for i in range(board.row):
                for j in range(board.col):
                    if board.board[i][j].is_king and board.board[i][j].color == "B":
                        result += 1
        else:
            for i in range(board.row):
                for j in range(board.col):
                    if board.board[i][j].is_king and board.board[i][j].color == "W":
                        result += 1
        return result

    def count_on_edge(self, board, color):
        result = 0
        if color == 1:
            for i in range(board.row):
                if board.board[i][0].color == "B":
                    result += 1
                if board.board[i][board.col].color == "B":
                    result += 1
            for j in range(board.col):
                if board.board[0][j].color == "B":
                    result += 1
                if board.board[board.row][j].color == "B":
                    result += 1
        else:
            for i in range(board.row):
                if board.board[i][0].color == "W":
                    result += 1
                if board.board[i][board.col].color == "W":
                    result += 1
            for j in range(board.col):
                if board.board[0][j].color == "W":
                    result += 1
                if board.board[board.row][j].color == "W":
                    result += 1
        return result

    def checker_num_heuristic(self, board, color):
        if color == 1:
            return board.black_count - board.white_count
        else:
            return board.white_count - board.black_count

    def king_num_heuristic(self, board, color):
        if color == 1:
            return (board.black_count - board.white_count) + (self.count_kings(board, color) - self.count_kings(board, 2))* 2
        else:
            return (board.white_count - board.black_count) + (self.count_kings(board, color) - self.count_kings(board, 1))* 2

    def on_edge_heuristic(self, board, color):
        return self.count_on_edge(board, color) * 1.5

    def count_kings_and_pawns(self, board, color):
        black_kings = 0
        black_pawns = 0
        white_kings = 0
        white_pawns = 0
        for row in range(board.row):
            for col in range(board.col):
                checker = board.board[row][col]
                if checker.color == "B":
                    if checker.is_king:
                        black_kings += 1
                    else:
                        black_pawns += 1
                elif checker.color == "W":
                    if checker.is_king:
                        white_kings += 1
                    else:
                        white_pawns += 1
        if color == 1:
            return (1.5*black_kings + black_pawns) - (1.5*white_kings + white_pawns)
        else:
            return (1.5*white_kings + white_pawns) - (1.5*black_kings + black_pawns)

    def count_kings_and_pawns_with_distance(self, board, color):
        black_score = 0
        white_score = 0
        for row in range(board.row):
            for col in range(board.col):
                checker = board.board[row][col]
                if checker.color == "B":
                    if checker.is_king:
                        black_score += 1.5
                    else:
                        black_score += 1
                elif checker.color == "W":
                    if checker.is_king:
                        white_score += 1.5
                    else:
                        white_score += 1
        if color == 1:
            return black_score - white_score
        else:
            return white_score - black_score


    def minimax(self,board,color,depth):
        opposite = self.opposite_color(color)
        moves = board.get_all_possible_moves(color)
        best_move = moves[0][0]
        best_score = float('-inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.min(board, opposite,depth-1)
                board.undo()
                if score > best_score:
                    best_move = moves[i][j]
                    best_score = score
        return best_move

    def min(self,board,color,depth):
        opposite = self.opposite_color(color)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board,color)
        moves = board.get_all_possible_moves(color)
        best_score = float('inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.max(board,opposite,depth-1)
                board.undo()
                if score < best_score:
                    best_score = score
        return best_score

    def max(self,board,color,depth):
        opposite = self.opposite_color(color)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board, color)
        moves = board.get_all_possible_moves(color)
        best_score = float('-inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.min(board, opposite,depth-1)
                board.undo()
                if score > best_score:
                    best_score = score
        return best_score


    def opposite_color(self,color):
        return self.opponent[color]


    def opponent_letter(self):
        if self.color == 1:
            return 'W'
        else:
            return 'B'


    def filter_lose_move(self, moves, index):
        board = self.board.board
        new_pos = moves[index[0][0]][index[0][1]].seq[-1]
        x = new_pos[0]
        y = new_pos[1]
        if self.board.is_in_board(x + 1, y + 1) and self.board.is_in_board(x - 1, y - 1):
            if board[x + 1][y + 1].color == self.opponent_letter() and board[x - 1][y - 1].color == ".":
                if self.color == 1:
                    return False
                else:
                    if board[x + 1][y + 1].is_king:
                        return False
            if board[x + 1][y + 1].color == "." and board[x - 1][y - 1].color == self.opponent_letter():
                if self.color == 2:
                    return False
                else:
                    if board[x - 1][y - 1].is_king:
                        return False
        if self.board.is_in_board(x + 1, y - 1) and self.board.is_in_board(x - 1, y + 1):
            if (board[x + 1][y - 1].color == self.opponent_letter()) and (board[x - 1][y + 1].color == "."):
                if self.color == 1:
                    return False
                else:
                    if board[x + 1][y - 1].is_king:
                        return False
            if (board[x + 1][y - 1].color == "." ) and (board[x - 1][y + 1].color == self.opponent_letter()):
                if self.color == 2:
                    return False
                else:
                    if board[x - 1][y + 1].is_king:
                        return False
        return True



    def alpha_beta_search(self,board,color,depth):
        opposite = self.opposite_color(color)
        moves = board.get_all_possible_moves(color)
        best_move = moves[0][0]
        alpha = float('-inf')
        beta = float('inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = self.min_value(board, opposite,depth-1,alpha,beta)
                board.undo()
                if score > alpha:
                    best_move = moves[i][j]
                    alpha = score
        return best_move

    def min_value(self,board,color,depth,al,be):
        opposite = self.opposite_color(color)
        #moves = board.get_all_possible_moves(color)
        #count_moves = 0
        #for c in moves:
            #count_moves += len(c)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board,color)
            #return self.count_kings_and_pawns_with_distance(board, color)
            #return self.count_kings_and_pawns_with_distance(board, color) + count_moves * 0.5
            # return self.king_num_heuristic(board, color) + self.on_edge_heuristic(board, color)
        moves = board.get_all_possible_moves(color)
        score = float('inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = min(score, self.max_value(board,opposite,depth-1,al,be))
                board.undo()
                if score <= al:
                    return score
                be = min(be, score)
        return be

    def max_value(self,board,color,depth,al,be):
        opposite = self.opposite_color(color)
        #moves = board.get_all_possible_moves(color)
        #count_moves = 0
        #for c in moves:
        #    count_moves += len(c)
        if depth == 0 or board.is_win(opposite) == (0 or 1 or 2):
            return self.checker_num_heuristic(board, color)
            #return self.count_kings_and_pawns_with_distance(board, color)
            #return self.count_kings_and_pawns_with_distance(board,color) + count_moves * 0.5
        moves = board.get_all_possible_moves(color)
        score = float('-inf')
        for i in range(len(moves)):
            for j in range(len(moves[i])):
                board.make_move(moves[i][j], color)
                score = max(score, self.min_value(board, opposite,depth-1,al,be))
                board.undo()
                if score >= be:
                    return score
                al = max(al,score)
        return score








