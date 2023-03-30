"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate 
all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""



def decompressRLElist(nums: list[int]) -> list[int]:

    res = []

    for i in range(len(nums)):
        if i % 2 != 0:
            continue

        res.extend([nums[i + 1]] * nums[i])
    return res