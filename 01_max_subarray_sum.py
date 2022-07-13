"""
Given an array of integers, the task is to find the maximum subarray sum possible of all the non-empty subarrays.
Subarrays are arrays inside another array which only contains contiguous elements.
"""

INT_MIN = -(2**31)


def max_subarray_sum1(nums: list[int]) -> int:
    """
    Simple approach.

    Time complexity: O(n^2), where n is the size of the array.

    Space complexity: O(1).

    """
    n = len(nums)
    max_sum = INT_MIN

    for i in range(0, n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum + nums[j]
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum


if __name__ == "__main__":
    a = [1, 3, 8, -2, 6, -8, 5]
    b = [1, 2, 3, 0, 3]
    c = [4, 2, 9, 7, 19]
    d = [2, -1, 1]
    print("== Simple approach ==")
    print(f"nums={a}", "returns:", max_subarray_sum1(a))
    print(f"nums={b}", "returns:", max_subarray_sum1(b))
    print(f"nums={c}", "returns:", max_subarray_sum1(c))
    print(f"nums={d}", "returns:", max_subarray_sum1(d))
