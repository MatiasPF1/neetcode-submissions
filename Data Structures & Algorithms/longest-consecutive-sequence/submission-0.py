class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)                       #eliminate reptitive ones
        longest = 0                            
        for i in nums:
            if i - 1 not in nums:
                counter = 1
                while i + counter in nums:
                    counter += 1
                longest = max(longest, counter)
        return longest



        