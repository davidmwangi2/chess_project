
# main.py
import pygame, sys, chess
from constants import WIDTH, HEIGHT
from db import init_db, create_game
from board import BoardView, ChessGame

def main():
    pygame.init()
    pygame.display.set_caption("Pygame Chess")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    init_db()
    game_id = create_game("White", "Black")
    controller = ChessGame(game_id)
    ui = BoardView(screen, controller)
    ui.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
