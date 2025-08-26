
import copy
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Pawns
        for col in range(8):
            self.grid[6][col] = Pawn('white')
            self.grid[1][col] = Pawn('black')

        # Rooks
        self.grid[7][0] = Rook('white')
        self.grid[7][7] = Rook('white')
        self.grid[0][0] = Rook('black')
        self.grid[0][7] = Rook('black')

        # Knights
        self.grid[7][1] = Knight('white')
        self.grid[7][6] = Knight('white')
        self.grid[0][1] = Knight('black')
        self.grid[0][6] = Knight('black')

        # Bishops
        self.grid[7][2] = Bishop('white')
        self.grid[7][5] = Bishop('white')
        self.grid[0][2] = Bishop('black')
        self.grid[0][5] = Bishop('black')

        # Queens
        self.grid[7][3] = Queen('white')
        self.grid[0][3] = Queen('black')

        # Kings
        self.grid[7][4] = King('white')
        self.grid[0][4] = King('black')

    def get_piece(self, pos):
        row, col = pos
        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]
        return None

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        piece = self.get_piece(start)
        if piece:
            self.grid[er][ec] = piece
            self.grid[sr][sc] = None

    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                piece = self.get_piece((r,c))
                if piece and piece.name == 'King' and piece.color == color:
                    return (r, c)
        return None

    def copy(self):
        return copy.deepcopy(self)

    def print_board(self):
        piece_to_char = {
            'Pawn': 'P',
            'Rook': 'R',
            'Knight': 'N',
            'Bishop': 'B',
            'Queen': 'Q',
            'King': 'K'
        }
        for row in self.grid:
            row_str = ''
            for piece in row:
                if piece is None:
                    row_str += '. '
                else:
                    char = piece_to_char.get(piece.name, '?')
                    if piece.color == 'black':
                        char = char.lower()
                    row_str += char + ' '
            print(row_str)
        print()

