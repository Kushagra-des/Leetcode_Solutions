class Solution {
public:
    int numberOfSets(int n, int k) {
        const int MOD = 1e9 + 7;

        vector<long long> dp(k + 1, 0);
        vector<long long> end(k + 1, 0);

        dp[0] = 1;

        for (int i = 1; i < n; i++) {
            for (int j = k; j >= 1; j--) {
                // Start a new segment or extend the last segment
                end[j] = (end[j] + dp[j - 1]) % MOD;

                // Segment ends at current point
                dp[j] = (dp[j] + end[j]) % MOD;
            }
        }

        return dp[k];
    }
};