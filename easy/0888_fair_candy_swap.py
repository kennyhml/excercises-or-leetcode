"""
Alice and Bob have a different total number of candies. You are given two integer 
arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of 
the ith box of candy that Alice has and bobSizes[j] is the number of candies 
of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that 
after the exchange, they both have the same total amount of candy. The total 
amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in 
the box that Alice must exchange, and answer[1] is the number of candies in the 
box that Bob must exchange. If there are multiple answers, you may return any 
one of them. It is guaranteed that at least one answer exists.

EXPLANATION:

The amount we have to exchange is (sum(a) - sum(b)) / 2 consider a = [1, 1] and b = [2, 2] then (2 - 4) / 2 = -1, 
if we exchange with a total change of 1, then sum a will be 3 and sum b will be 3 as well, thus its fair.

Meaning all we have to do whether a candy exists within b so that this candy + the diff exists in a.
"""

def fairCandySwap(aliceSizes: list[int], bobSizes: list[int]) -> list[int]:

    diff = (sum(aliceSizes) - sum(bobSizes)) / 2
    aliceSizes = set(aliceSizes)

    for candy in set(bobSizes):
        if diff + candy in aliceSizes:
            return [diff + candy, candy]