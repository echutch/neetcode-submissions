class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)

        for c in t:
            t_freq[c] += 1

        min_str = ""
        min_len = len(s) + 1

        w_freq = defaultdict(int)
        have = 0
        need = len(t_freq)

        l = 0
        for r in range(len(s)):
            c = s[r]
            w_freq[c] += 1
            
            if c in t_freq and w_freq[c] == t_freq[c]:
                have += 1

            while have == need:
                curr_str = s[l : r + 1]
                if len(curr_str) < min_len:
                    min_len = len(curr_str)
                    min_str = curr_str

                w_freq[s[l]] -= 1
                if s[l] in t_freq and w_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        return min_str
            

           

            

        