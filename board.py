
# board.py
import pygame
import chess
from pieces import load_piece_images

class ChessGame:
    def __init__(self, game_id, width=640, height=640):
        self.game_id = game_id
        self.board = chess.Board()

        # Setup pygame window
        self.width = width
        self.height = height
        self.square_size = width // 8
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess Game")

        # Load piece images
        self.images = load_piece_images(self.square_size)

        # Game state
        self.running = True
        self.selected_square = None  
        self.dragging_piece = None   
        self.drag_offset = (0, 0)

    def draw_board(self):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(col * self.square_size, row * self.square_size,
                                self.square_size, self.square_size)
                )

    def draw_pieces(self, mouse_pos=None):
        """Draw pieces, except the one being dragged."""
        for row in range(8):
            for col in range(8):
                square_index = (7 - row) * 8 + col
                piece = self.board.piece_at(square_index)
                if piece:
                    symbol = piece.symbol()
                    img = self.images.get(symbol)
                    if img:
                        # Don't draw the piece being dragged
                        if self.dragging_piece and square_index == self.selected_square:
                            continue
                        self.screen.blit(img, (col * self.square_size, row * self.square_size))

        # Draw dragging piece following mouse
        if self.dragging_piece and mouse_pos:
            img = self.images.get(self.dragging_piece.symbol())
            if img:
                x, y = mouse_pos
                self.screen.blit(img, (x - self.drag_offset[0], y - self.drag_offset[1]))

    def pos_to_square(self, pos):
        """Convert mouse position to a chess square index."""
        x, y = pos
        col = x // self.square_size
        row = y // self.square_size
        return (7 - row) * 8 + col  # chess.Board indexing

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    square = self.pos_to_square(event.pos)
                    piece = self.board.piece_at(square)
                    if piece and (
                        (piece.color and self.board.turn) or
                        (not piece.color and not self.board.turn)
                    ):
                        self.selected_square = square
                        self.dragging_piece = piece
                        col = event.pos[0] % self.square_size
                        row = event.pos[1] % self.square_size
                        self.drag_offset = (col, row)

                elif event.type == pygame.MOUSEBUTTONUP and self.dragging_piece:
                    target_square = self.pos_to_square(event.pos)
                    move = chess.Move(self.selected_square, target_square)

                    if move in self.board.legal_moves:
                        self.board.push(move)  # make valid move

                    # reset drag state
                    self.dragging_piece = None
                    self.selected_square = None

            # Draw everything
            self.draw_board()
            self.draw_pieces(mouse_pos)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

