class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        for str in strs:
            anagram = ''.join(sorted(str))

            if hash_map.get(anagram) == None:
                hash_map[anagram] = []

            hash_map[anagram].append(str)

        
        return list(hash_map.values())