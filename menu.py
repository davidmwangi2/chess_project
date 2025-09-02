def display_menu():
    print("=== Chess Game Menu ===")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. View Instructions")
    print("4. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in range(1, 5):
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    display_menu()
    choice = get_user_choice()
    print(f"You selected option {choice}.")