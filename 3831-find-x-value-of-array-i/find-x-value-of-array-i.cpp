class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> ans(k, 0);
        vector<long long> dp(k, 0);

        for (int x : nums) {
            vector<long long> ndp(k, 0);

            // Start a new subarray with x
            ndp[x % k]++;

            // Extend every subarray ending at the previous position
            for (int r = 0; r < k; r++) {
                int nr = (1LL * r * x) % k;
                ndp[nr] += dp[r];
            }

            // Every subarray ending here contributes to the answer
            for (int r = 0; r < k; r++) {
                ans[r] += ndp[r];
            }

            dp = move(ndp);
        }

        return ans;
    }
};