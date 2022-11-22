import random

gridMapping = {
        1: 0,
        2: 2,
        3: 4,
        4: 6,
        5: 8,
        6: 10,
        7: 12,
        8: 14,
        9: 16
    }

def play():
    grid = " | | \n | | \n | | "
    turn = 1
    while True:
        if ' ' not in grid:
            return 'X'
        square = int(input("Enter a number from 1-9 to choose square: "))
        idx = gridMapping[square]
        if grid[idx] != ' ':
            print("invalid selection, try again")
            continue
        else:
            if turn == 1:
                grid = grid[:idx] + 'X' + grid[idx+1:]
                turn = 2
            else:
                grid = grid[:idx] + 'O' + grid[idx+1:]
                turn = 1
        
        print(grid)

        if checkWinner(grid):
            break
        if ' ' not in grid:
            return 3
    
    return turn

def checkWinner(grid):
    if grid[0] == grid[2] == grid[4] and grid[0] != ' ':
        return True
    elif grid[6] == grid[8] == grid[10] and grid[6] != ' ':
        return True
    elif grid[12] == grid[14] == grid[16] and grid[12] != ' ':
        return True
    elif grid[0] == grid[6] == grid[12] and grid[0] != ' ':
        return True
    elif grid[2] == grid[8] == grid[14] and grid[2] != ' ':
        return True
    elif grid[4] == grid[10] == grid[16] and grid[4] != ' ':
        return True
    elif grid[0] == grid[8] == grid[16] and grid[0] != ' ':
        return True
    elif grid[12] == grid[8] == grid[4] and grid[12] != ' ':
        return True


winner = play()
if winner == 1:
    print("O Wins!")
elif winner == 2:
    print("X Wins!")
else:
    print("It's a draw!")
