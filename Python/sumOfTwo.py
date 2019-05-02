# Question: Given an unsorted array, find 2 elements that sum to 15.

arr1 = [4, 12, 21, 1, 5]
arr2 = [12, 7, 2, 1, 10, 3]


def sum_of_two(arr):
    arr.sort()
    print("Sorted Array: " + str(arr))
    for num, next_num in zip(arr[::], arr[1::]):
        if num + next_num == 15:
            return num, next_num
    return "No 2 elements add up to 15 in this array."


print("Arr1: " + str(sum_of_two(arr1)))
print("Arr2: " + str(sum_of_two(arr2)))
