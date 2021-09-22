"""
After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! 
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

"""

def matrixElementsSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    f = 0
    
    def determine(x,y):
        m = list(range(x))[::-1]
        for a in m:
            if matrix[a][y] == 0:
                return False  
        return True
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                continue
            if i == 0 and matrix[i][j] != 0:
                f+=matrix[i][j]
            else:
                res = determine(i,j)
                if res:
                    f+=matrix[i][j]
    return f   
