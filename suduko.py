def printsu(su):
    print("")
    print("Grid:")

    for x in range(9):
        if x % 3 == 0 and x != 0:
            for i in range(20):
                print("-", end ="")
            print("")              
        for y in range(9):
            if y % 3 == 0 and y!= 0:
                print("|", end = "")
            print(su[x][y], end =" ")
        print("")

def incolumn(su,a,b,value):
    for x in range(9):
        if su[x][b] == value :
                return True
    return False

def inrow(su,a,b,value):
    for x in range(9):
        if su[a][x] == value :
            return True
    return False

def ingrid(su,a,b,value):
    g1 = a // 3
    g2 = b // 3
    for x in range(g1*3,g1*3+3):
        for y in range(g2 * 3, g2 * 3 + 3):
            if su[x][y] == value :
                return True
    return False

def check(su,a,b,value):
    if incolumn(su, a, b, value) == False and inrow(su, a, b, value) == False and ingrid(su, a, b, value) == False:
        return True

def solvesu(su,a,b):
    if(a == 8 and b == 9):
        return True
    if(b == 9):
        a += 1
        b = 0
        if(su[a][b] != 0):
            return solvesu(su,a,b+1)
    for x in range(1,10):
        if check(su,a,b,x):
            su[a][b] = x
            if solvesu(su,a,b+1):
                return True
        su[a][b] = 0
    return False

su = [ [0]*9 for _ in range(9) ]
su = [
         [7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]
     ]

printsu(su)

T = solvesu(su,0,0)
printsu(su)
if T == False:
    print("puzzle is unsolvable")







