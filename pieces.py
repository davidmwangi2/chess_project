
class Piece:
    def __init__(self, color):
        self.color = color
        self.name = 'Piece'

    def get_valid_moves(self, pos, board):
        return []


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Pawn'

    def get_valid_moves(self, pos, board):
        moves = []
        row, col = pos
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1

        # Forward 1 square
        forward_pos = (row + direction, col)
        if board.get_piece(forward_pos) is None:
            moves.append(forward_pos)

            # Forward 2 squares from starting position
            if row == start_row:
                forward_two = (row + 2 * direction, col)
                if board.get_piece(forward_two) is None:
                    moves.append(forward_two)

        # Diagonal captures
        for dc in [-1, 1]:
            capture_pos = (row + direction, col + dc)
            target = board.get_piece(capture_pos)
            if target and target.color != self.color:
                moves.append(capture_pos)

        return [m for m in moves if 0 <= m[0] < 8 and 0 <= m[1] < 8]


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Knight'

    def get_valid_moves(self, pos, board):
        moves = []
        row, col = pos
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if not target or target.color != self.color:
                    moves.append((r, c))
        return moves


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Bishop'

    def get_valid_moves(self, pos, board):
        return self._slide_moves(pos, board, [(-1, -1), (-1, 1), (1, -1), (1, 1)])

    def _slide_moves(self, pos, board, directions):
        moves = []
        row, col = pos
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if not target:
                    moves.append((r, c))
                elif target.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Rook'

    def get_valid_moves(self, pos, board):
        return self._slide_moves(pos, board, [(-1, 0), (1, 0), (0, -1), (0, 1)])

    def _slide_moves(self, pos, board, directions):
        moves = []
        row, col = pos
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if not target:
                    moves.append((r, c))
                elif target.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'Queen'

    def get_valid_moves(self, pos, board):
        return self._slide_moves(pos, board, [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ])

    def _slide_moves(self, pos, board, directions):
        moves = []
        row, col = pos
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if not target:
                    moves.append((r, c))
                elif target.color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = 'King'

    def get_valid_moves(self, pos, board):
        moves = []
        row, col = pos
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.get_piece((r, c))
                if not target or target.color != self.color:
                    moves.append((r, c))
        return moves
