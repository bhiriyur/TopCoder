"""
Problem Statement
You are given a arr that contains a set of positive integers. The elements in arr are all distinct and they are given in increasing order.

A range is a finite set of consecutive integers. Formally, for any two positive integers a ≤ b the range [a,b] is defined to be the set of all integers that lie between a and b, inclusive. For example, [3,3] = {3} and [4,7] = {4,5,6,7}.

You want to represent the set given in arr as a union of some ranges. Return the minimum number of ranges you need.

Definition
Class: RangeEncoding
Method: minRanges
Parameters: tuple (integer)
Returns: integer
Method signature: def minRanges(self, arr):
Limits
Time limit (s): 2.000
Memory limit (MB): 256
Constraints
- arr will have between 1 and 50 elements, inclusive.
- Each element of arr will be between 1 and 50.
- The elements in arr will be in strictly increasing order.
Examples
0)
{1,2,3,4,5,6,7,8,9,10}
Returns: 1
We can represent this set as a single range [1,10].
1)
{1,6,10,20,32,49}
Returns: 6
In this case we have to use 6 different ranges, each containing just a single number.
2)
{2,4,5,6,8,9,10,11,12,15}
Returns: 4
This set of integers can be represented as the union of four ranges: [2,2], [4,6], [8,12], and [15,15].
3)
{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47}
Returns: 14
4)
{10,11,12,13,14,15,20,21,22,23,25,27,28,29,30,31,32,33}
Returns: 4
5)
{33}
Returns: 1
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
"""

class RangeEncoding:
    @staticmethod
    def minRanges(arr):
        n = len(arr)
        nranges = 1
        for i in range(1, n):
            if arr[i] - arr[i-1] > 1:
                nranges += 1
        return nranges