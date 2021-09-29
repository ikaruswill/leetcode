# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

from collections import defaultdict

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Reduce to a two-sum problem by summing all possible pairs
        two_sums = []
        pairs = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sums.append(nums[i] + nums[j])
                pairs.append((i, j))

        complements = defaultdict(list)
        quads = set([])
        for i, two_sum in enumerate(two_sums): # O(n/2)
            print(f'Eval {pairs[i]} : {two_sum}')
            if two_sum in complements:
                for pair_index in complements[two_sum]:
                    if (pairs[pair_index][0] != pairs[i][0] and \
                        pairs[pair_index][0] != pairs[i][1] and \
                        pairs[pair_index][1] != pairs[i][0] and \
                        pairs[pair_index][1] != pairs[i][1]): 
                        quad_index = (pairs[pair_index] + pairs[i])
                        quad = sorted([nums[q] for q in quad_index])
                        quads.add(tuple(quad))
            complements[target - two_sum].append(i)
            # print(complements)
            # print(res)
        return quads

def main(nums: list[int], target: int):
    s = Solution()
    print(s.fourSum(nums, target))


if __name__ == '__main__':
    main([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90],200)
