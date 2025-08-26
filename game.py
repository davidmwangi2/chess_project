
from board import Board

class Game:
    def __init__(self, board=None):
        self.board = board if board else Board()
        self.current_turn = 'white'
        self.game_over = False

    def play_turn(self, start_pos, end_pos):
        piece = self.board.get_piece(start_pos)
        if not piece or piece.color != self.current_turn:
            return False

        valid_moves = piece.get_valid_moves(start_pos, self.board)
        if end_pos not in valid_moves:
            return False

        self.board.move_piece(start_pos, end_pos)

        # After move, check for check or checkmate on opponent
        opponent = 'black' if self.current_turn == 'white' else 'white'

        if self.is_in_check(opponent):
            print(f"{opponent.capitalize()} is in check!")

            if self.is_checkmate(opponent):
                print(f"Checkmate! {self.current_turn.capitalize()} wins!")
                self.game_over = True

        if not self.game_over:
            self.current_turn = opponent

        return True

    def is_in_check(self, color):
        # TODO: Implement logic to check if `color` king is under attack
        pass

    def is_checkmate(self, color):
        # TODO: Implement logic to check if `color` has any legal moves to escape check
        pass
