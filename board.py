
# board.py
import pygame, chess
from constants import ROWS, COLS, SQUARE_SIZE, LIGHT_SQ, DARK_SQ, SELECT_BORDER
from pieces import load_piece_images
from db import add_move, game_moves

class ChessGame:
    def __init__(self, game_id):
        self.board = chess.Board()
        self.game_id = game_id
        # replay saved moves
        for move in game_moves(game_id):
            self.board.push_uci(move)

    def push(self, move):
        self.board.push(move)
        add_move(self.game_id, move.uci())

class BoardView:
    def __init__(self, screen, game: ChessGame):
        self.screen = screen
        self.game = game
        self.images = load_piece_images(SQUARE_SIZE)
        self.selected_square = None
        self.dragging_piece = None

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                color = LIGHT_SQ if (row+col) % 2 == 0 else DARK_SQ
                pygame.draw.rect(self.screen, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self):
        for square, piece in self.game.board.piece_map().items():
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            sym = piece.symbol()
            img = self.images.get(sym)
            if img:
                self.screen.blit(img, (col*SQUARE_SIZE, row*SQUARE_SIZE))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.draw_board()
            self.draw_pieces()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.on_release(event.pos)

            clock.tick(30)

    def on_click(self, pos):
        col = pos[0] // SQUARE_SIZE
        row = 7 - (pos[1] // SQUARE_SIZE)
        square = chess.square(col, row)
        piece = self.game.board.piece_at(square)
        if piece and ((piece.color and self.game.board.turn) or (not piece.color and not self.game.board.turn)):
            self.selected_square = square

    def on_release(self, pos):
        if self.selected_square is None:
            return
        col = pos[0] // SQUARE_SIZE
        row = 7 - (pos[1] // SQUARE_SIZE)
        target = chess.square(col, row)

        move = chess.Move(self.selected_square, target)
        if move in self.game.board.legal_moves:
            self.game.push(move)

        self.selected_square = None
