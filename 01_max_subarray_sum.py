"""
Given an array of integers, the task is to find the maximum subarray sum possible of all the non-empty subarrays.
Subarrays are arrays inside another array which only contains contiguous elements.
"""

import csv
from utils.time import chrono

INT_MIN = -(2**31)


def max_subarray_sum1(nums: list[int]) -> int:
    """
    Cumulative sum.
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


def max_subarray_sum2(nums: list[int]) -> int:
    """
    Kadane's algorithm. Dynamic programming.
    Time complexity: O(n), where n is the size of the array.
    Space complexity: O(1).

    """
    n = len(nums)
    max_sum = INT_MIN
    curr_sum = 0

    for i in range(0, n):
        curr_sum = curr_sum + nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


if __name__ == "__main__":
    a = [1, 3, 8, -2, 6, -8, 5]
    b = [1, 2, 3, 0, 3]
    c = [4, 2, 9, 7, 19]
    d = [2, -1, 1]
    e = []

    with open("assets/15000_numbers.csv", "r") as fd:
        reader = csv.reader(fd)
        for row in reader:
            e.extend(row)

    e = [int(i) for i in e]

    print("== Cumulative sum ==")
    ret = chrono(max_subarray_sum1, a)
    print(f"nums={a},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum1, b)
    print(f"nums={b},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum1, c)
    print(f"nums={c},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum1, d)
    print(f"nums={d},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum1, e)
    print("15000 numbers,", "returns:", f"{ret.rval},", "takes:", ret.time)

    print()
    print("== Kadane's algorithm ==")
    ret = chrono(max_subarray_sum2, a)
    print(f"nums={a},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum2, b)
    print(f"nums={b},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum2, c)
    print(f"nums={c},", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum2, d)
    print(f"nums={d}", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(max_subarray_sum2, e)
    print("15000 numbers,", "returns:", f"{ret.rval},", "takes:", ret.time)
