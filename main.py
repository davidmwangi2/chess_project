
from game import Game

def parse_input(input_str):
    try:
        start_str, end_str = input_str.strip().lower().split()
        start = (8 - int(start_str[1]), ord(start_str[0]) - ord('a'))
        end = (8 - int(end_str[1]), ord(end_str[0]) - ord('a'))
        return start, end
    except:
        return None, None

def main():
    game = Game()

    while not game.game_over:
        print(f"\n{game.current_turn.capitalize()}'s move:")
        game.board.print_board()

        move_input = input("Enter move (e.g., e2 e4): ")
        start, end = parse_input(move_input)

        if start is None or end is None:
            print("Invalid input format. Use e.g., 'e2 e4'")
            continue

        success = game.play_turn(start, end)
        if not success:
            print("Invalid move. Try again.")

    print("Game over.")
    game.board.print_board()

if __name__ == "__main__":
    main()
