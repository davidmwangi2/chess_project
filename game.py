
from board import Board
import copy

class Game:
    def __init__(self, board=None):
        self.board = board if board else Board()
        self.current_turn = 'white'
        self.game_over = False

    def play_turn(self, start_pos, end_pos):
        piece = self.board.get_piece(start_pos)
        if not piece or piece.color != self.current_turn:
            print("Invalid move: No piece of yours at the start position.")
            return False

        valid_moves = piece.get_valid_moves(start_pos, self.board)
        if end_pos not in valid_moves:
            print("Invalid move: Move not valid for that piece.")
            return False

        # Check if the move leaves your king in check
        new_board = self.board.copy()
        new_board.move_piece(start_pos, end_pos)
        if self.is_in_check_after_move(new_board, self.current_turn):
            print("Invalid move: You cannot leave your king in check.")
            return False

        # Make the move on the actual board
        self.board.move_piece(start_pos, end_pos)

        opponent = 'black' if self.current_turn == 'white' else 'white'

        # Check/checkmate/stalemate detection
        if self.is_in_check(opponent):
            print(f"{opponent.capitalize()} is in check!")
            if self.is_checkmate(opponent):
                print(f"Checkmate! {self.current_turn.capitalize()} wins!")
                self.game_over = True
        elif self.is_stalemate(opponent):
            print("Stalemate! It's a draw.")
            self.game_over = True

        if not self.game_over:
            self.current_turn = opponent

        return True

    def is_in_check(self, color):
        king_pos = self.board.find_king(color)
        opponent = 'black' if color == 'white' else 'white'

        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece and piece.color == opponent:
                    moves = piece.get_valid_moves((r, c), self.board)
                    if king_pos in moves:
                        return True
        return False

    def is_in_check_after_move(self, new_board, color):
        original_board = self.board
        self.board = new_board
        in_check = self.is_in_check(color)
        self.board = original_board
        return in_check

    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False

        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece and piece.color == color:
                    moves = piece.get_valid_moves((r, c), self.board)
                    for move in moves:
                        new_board = self.board.copy()
                        new_board.move_piece((r, c), move)
                        if not self.is_in_check_after_move(new_board, color):
                            return False
        return True

    def is_stalemate(self, color):
        if self.is_in_check(color):
            return False

        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece and piece.color == color:
                    moves = piece.get_valid_moves((r, c), self.board)
                    for move in moves:
                        new_board = self.board.copy()
                        new_board.move_piece((r, c), move)
                        if not self.is_in_check_after_move(new_board, color):
                            return False
        return True


    