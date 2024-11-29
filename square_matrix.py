def square_matrix(matrix):
    rows = len(matrix)    
    cols = len(matrix[0]) 
    
    result = [[0]*cols for _ in range(rows)]
    for i in range(cols):
        for j in range(rows):
            result[j][i] = matrix[j][i] ** 2
    
    return result
    
print(square_matrix([[1, 2], [3, 4]]))

#Напишите функцию square_matrix, которая принимает квадратную матрицу (список списков) и возвращает матрицу, где каждый элемент возведён в квадрат.