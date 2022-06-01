matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_matrix = []

def diagonal(matrix):
    diagonal_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                diagonal_matrix.append(matrix[i][j])
    print(diagonal_matrix)
    return diagonal_matrix
    
diagonal(matrix)

m = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4] ]
def transpose(m):

    t = []
    t = [[row[i] for row in m] for i in range(len(m[0]))]
    print(t)
    return t

transpose(m)
