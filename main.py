
from game import Game
from utils import parse_input

def main():
    game = Game()

    while True:
        game.board.display()
        print(f"{game.current_turn.capitalize()}'s move.")
        user_input = input("Enter move (e.g., e2 e4): ")
        
        try:
            start_str, end_str = user_input.strip().split()
            start = parse_input(start_str)
            end = parse_input(end_str)
        except:
            print("Invalid input format. Use e.g. 'e2 e4'")
            continue

        if not game.play_turn(start, end):
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
