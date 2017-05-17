class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for(int i = 0; i < nums.size(); ++i) {
            int x = target - nums[i];
            auto it = seen.find(x);
            if(it != seen.end()) {
                return {it->second, i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
