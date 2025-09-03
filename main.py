
# main.py
import pygame
from board import ChessGame
from db import init_db, new_game   

def main():
    # Initialize pygame
    pygame.init()

    #  Initialize database (your function from db.py, not pygame)
    init_db()

    #  Create a new game entry
    game_id = new_game()

    # Start the chess game GUI
    game = ChessGame(game_id)
    game.run()

if __name__ == "__main__":
    main()



