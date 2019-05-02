# Given 1 to n integers in array of length n + 2, there are 2 numbers which are repeated. Find the repeated numbers.


def print_repeating(arr1, size):
    count = [0] * size
    print(" Repeating elements are ", end="")
    for i in range(0, size):
        if count[arr1[i]] == 1:
            print(arr1[i], end=" ")
        else:
            count[arr1[i]] = count[arr[i]] + 1


# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
print_repeating(arr, arr_size)
