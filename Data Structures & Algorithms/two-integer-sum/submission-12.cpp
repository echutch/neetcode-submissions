#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        diff.reserve(nums.size());

        for (int i = 0; i < nums.size(); i++) {
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
