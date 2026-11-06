#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            int check_diff = target - nums[i];
            if (diff.find(check_diff) != diff.end()) {
                return {diff[check_diff], i};
            } else {
                diff.insert({nums[i], i});
            }
        }
        return {};
    }
};
