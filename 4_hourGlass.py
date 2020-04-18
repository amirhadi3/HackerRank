import math


# Complete the hourglassSum function below.
def hourglassSum(arr):
    num_of_rows = len(arr)
    num_of_columns = len(arr[0])
    max_value = -math.inf

    for row_index in range(0, num_of_rows - 2):
        for col_index in range(0, num_of_columns - 2):
            sum_value = 0
            sub_array = [arr[row_index][col_index:col_index + 3] \
                , [arr[row_index + 1][col_index + 1]] \
                , arr[row_index + 2][col_index:col_index + 3]]
            for array in sub_array:
                sum_value += sum(array)

            if sum_value > max_value:
                max_value = sum_value

    return max_value


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], \
           [0, 1, 0, 0, 0, 0], \
           [1, 1, 1, 0, 0, 0], \
           [0, 0, 2, 4, 4, 0], \
           [0, 0, 0, 2, 0, 0], \
           [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)

    print(result)
