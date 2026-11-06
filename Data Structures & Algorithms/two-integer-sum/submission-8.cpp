#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            if (auto it = diff.find(nums[i]); it != diff.end()) {
                return {it->second, i};
            } else {
                diff[target - nums[i]] = i;
            }
        }
        return {};
    }
};
