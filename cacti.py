def cacti_number(mat):
    def wrapper():
        num_cacti = 0
        for i in range(0,len(mat)): #row
            for j in range(0, len(mat[0])): #col
                if mat[i][j] == 1:
                    continue
                if (i > 0 and mat[i-1][j] == 1) or (i < len(mat) - 1  and mat[i+1][j] == 1) or (j > 0 and mat[i][j - 1] == 1) or (j < len(mat[0]) - 1 and mat[i][j+1] == 1):
                    continue
                else:
                    num_cacti += 1
                    mat[i][j] = 1
        return num_cacti
    return wrapper

array =   [ [1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0] ]
print(cacti_number(array))

