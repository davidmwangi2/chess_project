
class Piece:
    def __init__(self, color):
        self.color = color

    def get_valid_moves(self, pos, board):
        # Override in subclasses
        return []

    def __str__(self):
        return self.symbol.upper() if self.color == 'white' else self.symbol.lower()


class Pawn(Piece):
    symbol = 'P'

    def get_valid_moves(self, pos, board):
        row, col = pos
        direction = -1 if self.color == 'white' else 1
        moves = []

        # One step forward
        next_row = row + direction
        if 0 <= next_row < 8 and board.get_piece((next_row, col)) is None:
            moves.append((next_row, col))

            # Two steps forward from starting position
            start_row = 6 if self.color == 'white' else 1
            next_row2 = row + 2 * direction
            if row == start_row and board.get_piece((next_row2, col)) is None:
                moves.append((next_row2, col))

        # Pawn captures (diagonal)
        for dc in [-1, 1]:
            next_col = col + dc
            if 0 <= next_col < 8 and 0 <= next_row < 8:
                target = board.get_piece((next_row, next_col))
                if target and target.color != self.color:
                    moves.append((next_row, next_col))

        for dc in [-1, 1]:
            new_col = col + dc
            if 0 <= new_col < 8:
                target = board.get_piece((next_row, new_col))
                if target and target.color != self.color:
                    moves.append((next_row, new_col))

        return moves


class Knight(Piece):
    symbol = 'N'

    def get_valid_moves(self, pos, board):
        row, col = pos
        moves = []
        candidate_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2),
        ]

        for r, c in candidate_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if target is None or target.color != self.color:
                    moves.append((r, c))
        return moves


class Bishop(Piece):
    symbol = 'B'

    def get_valid_moves(self, pos, board):
        return self._get_sliding_moves(pos, board, directions=[(1,1), (1,-1), (-1,1), (-1,-1)])

    def _get_sliding_moves(self, pos, board, directions):
        moves = []
        row, col = pos
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if target is None:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
                r += dr
                c += dc
        return moves


class Rook(Piece):
    symbol = 'R'

    def get_valid_moves(self, pos, board):
        return self._get_sliding_moves(pos, board, directions=[(1,0), (-1,0), (0,1), (0,-1)])

    def _get_sliding_moves(self, pos, board, directions):
        moves = []
        row, col = pos
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if target is None:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
                r += dr
                c += dc
        return moves


class Queen(Piece):
    symbol = 'Q'

def get_valid_moves(self, pos, board):
    moves = []
    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # down-right diagonal
        (1, -1),  # down-left diagonal
        (-1, 1),  # up-right diagonal
        (-1, -1)  # up-left diagonal
    ]

    row, col = pos

    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            target_piece = board.get_piece((r, c))
            if target_piece is None:
                moves.append((r, c))
            else:
                if target_piece.color != self.color:
                    moves.append((r, c))  # Can capture opponent piece
                break  # Can't jump over pieces
            r += dr
            c += dc

    return moves



class King(Piece):
    symbol = 'K'

    def get_valid_moves(self, pos, board):
        row, col = pos
        moves = []
        candidate_moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1),
        ]

        for r, c in candidate_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if target is None or target.color != self.color:
                    moves.append((r, c))
        return moves
