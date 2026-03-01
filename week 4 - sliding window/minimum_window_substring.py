class Solution:

    def compareCounter(self, big, small):
        return all(big.get(key, 0) >= value for key, value in small.items())

    def minWindow(self, s: str, t: str) -> str:
        result = ""

        t_map = Counter(t)
        s_map = Counter()

        l = 0
        for r, r_char in enumerate(s):
            s_map[r_char] += 1

            while self.compareCounter(s_map, t_map):
                sub_string = s[l:r + 1] 

                if result == "" or len(sub_string) < len(result):
                    result = sub_string
                
                l_char = s[l]
                s_map[l_char] -= 1

                l += 1

        return result