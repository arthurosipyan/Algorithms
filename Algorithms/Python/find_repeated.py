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
print_repeating(arr, arr_size)  # O(n)

# ------------------------------------------------------------------------------------------------------------------

print("")
arr1 = [4, 2, 4, 5, 2, 3, 1]


def repeat_int(n):
    repeat = []
    for i in range(len(n)):
        j = i + 1
        for j in range(j, len(n)):
            if n[i] == n[j] and n[i] not in repeat:
                repeat.append(n[i])
    return repeat


print(repeat_int(arr1))     # O(n^2)
