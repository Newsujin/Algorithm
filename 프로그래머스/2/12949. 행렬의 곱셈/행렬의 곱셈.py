def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr2_col = len(arr2[0])
    common_len = len(arr2)

    res = [[0] * arr2_col for _ in range(arr1_row)]

    for i in range(arr1_row):
        for j in range(arr2_col):
            for k in range(common_len):
                res[i][j] += arr1[i][k] * arr2[k][j]

    return res