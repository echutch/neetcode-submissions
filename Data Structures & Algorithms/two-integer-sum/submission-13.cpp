#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const int n = static_cast<int>(nums.size());
        unordered_map<int, int> diff;
        diff.reserve(n);

        for (int i = 0; i < n; i++) {
            const int curr_num = nums[i];

            const int complement = target - curr_num;

            if (auto it = diff.find(complement); it != diff.end()) {
                return {it->second, i};
            } 
            diff[curr_num] = i;
        }
        return {};
    }
};
