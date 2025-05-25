from random import randrange

def display_board(board):
    """Display the game board with current moves"""
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    """Handle user's move and update the board"""
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Move must be between 1 and 9")
                continue
            
            # Convert move number to board coordinates
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if isinstance(board[row][col], int):
                board[row][col] = 'O'
                break
            else:
                print("That square is already occupied!")
        except ValueError:
            print("Please enter a valid number!")

def make_list_of_free_fields(board):
    """Return list of available squares as (row, col) tuples"""
    free = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free.append((row, col))
    return free

def victory_for(board, sign):
    """Check if the player with the given sign has won"""
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    
    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    return False

def draw_move(board):
    """Handle computer's move and update the board"""
    free = make_list_of_free_fields(board)
    if free:  # If there are free fields left
        # Computer plays 'X' in a random free field
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

def main():
    """Main game loop"""
    # Initialize board with numbers 1-9
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Computer makes first move (center square)
    board[1][1] = 'X'
    display_board(board)
    
    while True:
        # Player's move
        enter_move(board)
        display_board(board)
        
        # Check if player won
        if victory_for(board, 'O'):
            print("You won!")
            break
            
        # Check for tie
        if not make_list_of_free_fields(board):
            print("Tie game!")
            break
            
        # Computer's move
        draw_move(board)
        display_board(board)
        
        # Check if computer won
        if victory_for(board, 'X'):
            print("Computer won!")
            break
            
        # Check for tie
        if not make_list_of_free_fields(board):
            print("Tie game!")
            break

if __name__ == "__main__":
    main()