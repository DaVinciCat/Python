def square_matrix(sq_matrix):
    rows = len(sq_matrix)    
    cols = len(sq_matrix[0]) 
    
    result = [[0]*cols for _ in range(rows)]
    for i in range(cols):
        for j in range(rows):
            result[i][j] = sq_matrix[i][j] ** 2
    
    return result
    
print(square_matrix([[1, 2], [3, 4]]))

#Напишите функцию square_matrix, которая принимает квадратную матрицу (список списков) и возвращает матрицу, где каждый элемент возведён в квадрат.