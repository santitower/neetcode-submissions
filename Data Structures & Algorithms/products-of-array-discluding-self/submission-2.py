class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # O(n^2) time
        '''for i in range(len(nums)):
            product = 1
            left = nums[:i]
            right = nums[i + 1:]
            for num in left:
                product *= num
            for num in right:
                product *= num
            result.append(product)'''

        prefix = []
        suffix = []
        product = 1
        for num in reversed(nums):
            suffix.append(product)
            product *= num
        suffix.reverse()

        product = 1

        for  num in nums:
            prefix.append(product)
            product *= num

        for i in range(len(nums)):
            result.append(suffix[i] * prefix[i])
        return result








        