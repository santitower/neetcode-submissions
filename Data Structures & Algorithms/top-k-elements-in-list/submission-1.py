class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can store every element that we see into a dict and count appearance
        k_dict = {}
        for num in nums:
            k_dict[num] = k_dict.get(num,0) + 1
        sorted_nums = sorted(k_dict, key=k_dict.get, reverse = True)
        return sorted_nums[:k]
        #yield the top k values with just two of the top X of the array?
        