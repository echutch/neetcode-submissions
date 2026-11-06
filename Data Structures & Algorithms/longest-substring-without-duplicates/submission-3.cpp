class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> window;

        size_t maxLength = 0;
        unsigned l = 0;

        for (unsigned r = 0; r < s.size(); r++) {
            while (window.count(s[r])) {
                // next char in window, need to shift
                window.erase(s[l]);
                l++;
            }

            window.insert(s[r]);
            maxLength = std::max(maxLength, window.size());
        }
        return maxLength;
        
    }
};
