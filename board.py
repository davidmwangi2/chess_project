
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = self.initialize_board()

    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        # Add pawns
        for i in range(8):
            board[6][i] = Pawn('white')
            board[1][i] = Pawn('black')

        # Add other pieces
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, PieceClass in enumerate(piece_order):
            board[7][i] = PieceClass('white')
            board[0][i] = PieceClass('black')

        return board

    def get_piece(self, pos):
        row, col = pos
        return self.grid[row][col]

    def move_piece(self, start, end):
        piece = self.get_piece(start)
        self.grid[end[0]][end[1]] = piece
        self.grid[start[0]][start[1]] = None

    def display(self):
        for row in self.grid:
            print(" ".join([str(piece) if piece else '.' for piece in row]))
        print()
   
    def find_king(self, color):
        for r in range(8):
         for c in range(8):
            piece = self.get_piece((r, c))
            if piece and piece.name == 'King' and piece.color == color:
                return (r, c)
        return None
