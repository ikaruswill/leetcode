# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,0,1],[-1,-1,2]]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sums = set([])
        positives = []
        negatives = []
        zeroes = []

        # Sort for uniqueness in triplets
        nums.sort()

        for num in nums:
            if num == 0:
                zeroes.append(num)
            elif num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
        
        # Handle case of 3 zeroes
        if len(zeroes) >= 3:
            three_sums.add((0, 0, 0))

        # Handle case of zero presence
        unique_positives = set(positives)
        unique_negatives = set(negatives)
        
        if len(zeroes):
            for p in unique_positives:
                if -p in unique_negatives:
                    three_sums.add((-p, 0, p))
        
        # Handle case of zero absence
        ## Pairs of negatives vs unique positive complement
        for i, n1 in enumerate(negatives):
            for j, n2 in enumerate(negatives[i+1:]):
                if -(n1 + n2) in unique_positives:
                    three_sums.add((n1, n2, -(n1 + n2)))

        ## Pairs of positives vs unique negative complement
        for i, p1 in enumerate(positives):
            for j, p2 in enumerate(positives[i+1:]):
                if -(p1 + p2) in unique_negatives:
                    three_sums.add((-(p1 + p2), p1, p2))

        return three_sums


def main(nums: list[int]):
    s = Solution()
    print(s.threeSum(nums))


if __name__ == '__main__':
    main([-1,0,1,2,-1,-4])