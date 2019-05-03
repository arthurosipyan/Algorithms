# Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite
# large.


def sum_array(array):
    array_sum = 0
    for num in array:
        array_sum += num
    return array_sum


print(sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
