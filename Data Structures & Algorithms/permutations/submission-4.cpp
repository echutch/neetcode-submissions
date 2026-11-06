class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> picked(nums.size(), false);
        vector<int> perm;
        backtrack(nums, picked, perm);
        return res;
    }

    void backtrack(vector<int>& nums, vector<bool>& picked, vector<int>& perm) {
        if (perm.size() == nums.size()) {
            res.push_back(perm);
            return;
        }

        for (unsigned i = 0; i < nums.size(); ++i) {
            if (!picked[i]) {
                picked[i] = true;
                perm.push_back(nums[i]);
                backtrack(nums, picked, perm);
                perm.pop_back();
                picked[i] = false;
            }
        } 
    }
};
