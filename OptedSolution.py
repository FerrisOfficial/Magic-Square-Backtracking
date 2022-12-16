# Size of a square
N = int(input("N = "))

# Magic sum (each row, column and diagonal must have this sum)
MAGIC_SUM = int(N*(N*N+1)/2)

# Magic square
Tab = [[0 for i in range(N)] for j in range(N)]

# Array of used numbers
Used = [False for i in range(N*N+1)]

# Sums of diagonals
SUM_DIAG1 = 0
SUM_DIAG2 = 0

# Sums of each row and column
Sum_row = [0 for i in range(N)]
Sum_col = [0 for i in range(N)]

# Number of backtrack calls
operations = 0

def print_magic_square():
    for i in range(N):
        for j in range(N):
            print(Tab[i][j], end=" ")
        print()

def check_conditions(x, y, i):
    # If the sum of the row or column or diagonals 
    # is greater than the magic sum, skip it
    global SUM_DIAG1, SUM_DIAG2
    
    if i + Sum_row[y] > MAGIC_SUM: return False
    if i + Sum_col[x] > MAGIC_SUM: return False
    if x == y and i + SUM_DIAG1 > MAGIC_SUM: return False
    if x + y == N-1 and i + SUM_DIAG2 > MAGIC_SUM: return False

    return True

def check_edges(x, y, i):
    # If we are at end of the row or column or diagonals
    # and the sum is incorrect, skip it
    global SUM_DIAG1, SUM_DIAG2

    if x == N-1 and i + Sum_row[y] != MAGIC_SUM: return False
    if y == N-1 and i + Sum_col[x] != MAGIC_SUM: return False
    if x == y and x == N-1 and y == N-1 and i + SUM_DIAG1 != MAGIC_SUM: return False
    if x + y == N-1 and x == 0 and y == N-1 and i + SUM_DIAG2 != MAGIC_SUM: return False

    return True

def update_sums_in(x, y, i):
    # Put the number in the current cell
    # and update the sums
    global SUM_DIAG1, SUM_DIAG2

    Tab[y][x] = i
    Used[i] = True
    Sum_row[y] += i
    Sum_col[x] += i
    if x == y: SUM_DIAG1 += i
    if x + y == N-1: SUM_DIAG2 += i

def update_sums_out(x, y, i):
    # Remove the number from the current cell
    # and update the sums
    global SUM_DIAG1, SUM_DIAG2

    Tab[y][x] = 0
    Used[i] = False
    Sum_row[y] -= i
    Sum_col[x] -= i
    if x == y: SUM_DIAG1 -= i
    if x + y == N-1: SUM_DIAG2 -= i

def backtracking(x, y):
    global operations, SUM_DIAG1, SUM_DIAG2

    operations += 1
    print("operations: ", operations, end="\r")

    # If we reach end of the row, go to the next one
    if x == N: x, y = 0, y+1
    # If we reach end of the square, we have a solution
    if y == N: return True

    # If we reach end of row, we can deduce value
    if x == N-1:
        i = MAGIC_SUM - Sum_row[y]

        if i < 1 or i > N*N: return False
        if Used[i]: return False
        if not check_conditions(x, y, i): return False
        if not check_edges(x, y, i): return False
        
        update_sums_in(x, y, i)
        if backtracking(x+1, y): return True
        update_sums_out(x, y, i)

        return False

    # If we reach last row, we can deduce value
    if y == N-1:
        i = MAGIC_SUM - Sum_col[x]

        if i < 1 or i > N*N: return False
        if Used[i]: return False
        if not check_conditions(x, y, i): return False
        if not check_edges(x, y, i): return False
        
        update_sums_in(x, y, i)
        if backtracking(x+1, y): return True
        update_sums_out(x, y, i)

        return False
        

    # Try to put a number in the current cell
    for i in range(1, N*N+1):
        # If the number is already used, skip it
        if Used[i]: continue

        if not check_conditions(x, y, i): break
        if not check_edges(x, y, i): continue

        update_sums_in(x, y, i)

        # Go to the next cell
        if backtracking(x+1, y): return True

        update_sums_out(x, y, i)

    # If no number can be put in the current cell, return False
    return False

def main():
    if backtracking(0, 0):
        print("")
        print_magic_square()
    else:
        print("No solution")
    

if __name__ == "__main__":
    main()

