class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict()
        bucket_list = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            if hash_map.get(num) == None:
                hash_map[num] = 0

            hash_map[num] += 1

        for key in hash_map:
            val = hash_map[key]

            bucket_list[val].append(key)

        count = 0
        for entry in reversed(bucket_list):
            if len(entry) != 0:
                result += entry
                count += len(entry)

            if count == k:
                break

        return result

