class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int xr = 0;
        int zeros = 0;

        for (int x : nums) {
            xr ^= x;
            if (x == 0) zeros++;
        }

        if (xr != 0) return nums.size();
        if (zeros == nums.size()) return 0;
        return nums.size() - 1;
    }
};