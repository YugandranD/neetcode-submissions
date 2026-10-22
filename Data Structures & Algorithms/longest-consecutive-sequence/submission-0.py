class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest =0

        for num in nums:
            if (num-1) not in hs :
                length =1
                while (num +length) in hs:
                    length+=1

                longest = max(length,longest)

        return  longest