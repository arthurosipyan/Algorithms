# Read an n integer . For all non-negative integers i < n , print i^2. See the sample for details.
#
# Sample Input:
#
# 5
#
# Sample Output:
#
# 0
# 1
# 4
# 9
# 16

n = 5
a = -10


def non_negative_squares(num):
    if num < 0:
        print("Error: non-negative integers only")
        return

    i = 0
    while i < num:
        print(i**2)
        i += 1
    return


non_negative_squares(n)
print("")
non_negative_squares(a)
