"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""

from utils.time import chrono
import csv


def count_subarray_sum1(nums: list[int], k: int) -> int:
    """
    Cumulative sum.
    Time complexity: O(n^2). Considering every possible subarray takes O(n^2) time.
    Space complexity : O(1). Constant space is used.

    """
    n = len(nums)
    count = 0

    for i in range(0, n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum + nums[j]
            if curr_sum == k:
                count += 1

    return count


def count_subarray_sum2(nums: list[int], k: int) -> int:
    """
    Hashtable / Dictionary / Map
    Time complexity: O(n).
    Space complexity: O(n).

    """
    occur = {0: 1}
    count = 0
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]  # cumulative sum
        if curr_sum - k in occur:
            count += occur[curr_sum - k]
        if curr_sum in occur:
            occur[curr_sum] += 1
        else:
            occur[curr_sum] = 1
    return count


if __name__ == "__main__":
    a = [1, 3, 8, -2, 6, -8, 5]
    b = [1, 2, 3, 0, 3]
    c = [4, 2, 9, 7, 19]
    d = [2, -1, 1]
    e = [1, 1, 1]
    f = [1, 2, 3]
    g = []

    with open("assets/15000_numbers.csv", "r") as fd:
        reader = csv.reader(fd)
        for row in reader:
            g.extend(row)

    g = [int(i) for i in g]

    print("== Cumulative sum ==")
    ret = chrono(count_subarray_sum1, a, 5)
    print(f"nums={a} and k=5,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum1, b, 3)
    print(f"nums={b} and k=3,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum1, c, 1)
    print(f"nums={c} and k=1,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum1, d, 2)
    print(f"nums={d} and k=2,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum1, e, 2)
    print(f"nums={e} and k=2,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum1, f, 3)
    print(f"nums={f} and k=3,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum1, g, 6)
    print(f"15000 numbers and k=6,", "returns:", f"{ret.rval},", "takes:", ret.time)

    print()
    print("== Hash table ==")
    ret = chrono(count_subarray_sum2, a, 5)
    print(f"nums={a} and k=5,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum2, b, 3)
    print(f"nums={b} and k=3,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum2, c, 1)
    print(f"nums={c} and k=1,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum2, d, 2)
    print(f"nums={d} and k=2,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum2, e, 2)
    print(f"nums={e} and k=2,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum2, f, 3)
    print(f"nums={f} and k=3,", "returns:", f"{ret.rval},", "takes:", ret.time)
    ret = chrono(count_subarray_sum2, g, 6)
    print(f"15000 numbers and k=6,", "returns:", f"{ret.rval},", "takes:", ret.time)
