
class Move:
    def __init__(self, start_pos, end_pos, piece, captured=None):
        self.start = start_pos
        self.end = end_pos
        self.piece = piece
        self.captured = captured
