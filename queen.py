def printboard(board):

    print("Board:")

    for x in range(8):
        for y in range(8):
            print(board[x][y], end ="   ")
        print("")
    print("")


def incolumn(board,a,b):
    for x in range(8):
        if board[x][b]:
                return True
    return False


def inrow(board,a,b):
    for x in range(8):
        if board[a][x]:
            return True
    return False


def indaigonal(board,a,b):
    for x in range(1,9):
        if isvalid(a+x, b+x):
            if board[a+x][b+x]:
                return True
        if isvalid(a-x, b-x):
            if board[a-x][b-x]:
                return True
        if isvalid(a+x, b-x):
            if board[a+x][b-x]:
                return True
        if isvalid(a-x, b+x):
            if board[a-x][b+x]:
                return True
    return False

def isvalid(a,b):
    if a in range(8) and b in range(8):
        return True


def check(board,a,b):
    if incolumn(board, a, b) == False and inrow(board, a, b) == False and indaigonal(board, a, b) == False:
        return True


def solve(board,a,b,count):
    print("COUNT=",count)
    printboard(board)
    if count == 8:
        return True

    if b == 8:
        a += 1
        b = 0
    for x in range(a,8):
        for y in range(8):
            if board[x][y] == 0:
                if check(board, x, y):
                    board[x][y] = 1
                    print(x, y)
                    if solve(board,x,y,count+1):
                        return True
                board[x][y] = 0
    return False


board = [ [0]*8 for _ in range(8) ]

printboard(board)

T = solve(board,0,0,0)
printboard(board)

if T == False:
    print("puzzle is unsolvable")







