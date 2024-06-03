def solution(arr1, arr2):
    rows_arr1 = len(arr1)
    cols_arr2 = len(arr2[0])
    common_dim = len(arr2)
    
    result = [[0] * cols_arr2 for _ in range(rows_arr1)]
    
    for i in range(rows_arr1):
        for j in range(cols_arr2):
            for k in range(common_dim):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result
