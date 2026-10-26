class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = []
        for num in nums:
            if num not in num_list:
                num_list.append(num)
            else:
                return True
        return False


        