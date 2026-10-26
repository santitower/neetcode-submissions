class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_dict = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []
        for num in nums:
            k_dict[num] = k_dict.get(num,0) + 1
        for num, freq in k_dict.items():
            buckets[freq].append(num)

        for freq in range(len(buckets) - 1, 0 ,-1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        
        