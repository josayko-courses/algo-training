"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""

from collections import defaultdict


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
    n = len(nums)

    count = 0
    dict_cumsum = defaultdict(int)  # hashtable for storing the cumsum
    curr_sum = 0  # for cumulative sum at each index
    for i in range(0, n):  # upto the length of the nums array
        curr_sum += nums[i]  # cumulative sum in each index
        if curr_sum == k:  # if current cumsum is equal to target
            count += 1
        # if curr_sum - k in the dict, then let's say
        # curr_sum - k = some_val. so, curr_sum = k + some_val, means
        # if the some_val is already in the dictionary, then there
        # exists a subarray whose sum is k that has lead us to this
        # curr_sum. How lead us? by some_val + k = curr_sum
        # now if some_val occurs more than 1 time, means you have
        # that number of subarray to consider to the count
        # So you need to add that number of occurence of curr_sum - k
        # to the count
        # think about this with example nums list in the solution
        # [3,4,7,2,-3,1,4,2] and also with [3,4,7,2,-3,1,4,2, 1]
        if curr_sum - k in dict_cumsum:
            count += dict_cumsum[curr_sum - k]
        # add the curr_sum entry to the hashtable
        dict_cumsum[curr_sum] += 1
    # print(dict_cumsum)
    return count


if __name__ == "__main__":
    a = [1, 3, 8, -2, 6, -8, 5]
    b = [1, 2, 3, 0, 3]
    c = [4, 2, 9, 7, 19]
    d = [2, -1, 1]
    e = [1, 1, 1]
    f = [1, 2, 3]
    print("== Cumulative sum ==")
    print(f"nums={a}", "and k=5", "returns:", count_subarray_sum1(a, 5))
    print(f"nums={b}", "and k=3", "returns:", count_subarray_sum1(b, 3))
    print(f"nums={c}", "and k=1", "returns:", count_subarray_sum1(c, 1))
    print(f"nums={d}", "and k=2", "returns:", count_subarray_sum1(d, 2))
    print(f"nums={e}", "and k=2", "returns:", count_subarray_sum1(e, 2))
    print(f"nums={f}", "and k=3", "returns:", count_subarray_sum1(f, 3))

    print()
    print("== Hash table ==")
    print(f"nums={a}", "and k=5", "returns:", count_subarray_sum2(a, 5))
    print(f"nums={b}", "and k=3", "returns:", count_subarray_sum2(b, 3))
    print(f"nums={c}", "and k=1", "returns:", count_subarray_sum2(c, 1))
    print(f"nums={d}", "and k=2", "returns:", count_subarray_sum2(d, 2))
    print(f"nums={e}", "and k=2", "returns:", count_subarray_sum2(e, 2))
    print(f"nums={f}", "and k=3", "returns:", count_subarray_sum2(f, 3))
