class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();

        // Convert stones into prefix sums.
        for (int i = 1; i < n; ++i) {
            stones[i] += stones[i - 1];
        }

        // Base case: take all stones.
        int dp = stones[n - 1];

        // i >= 1 because every move must take at least 2 stones.
        for (int i = n - 2; i >= 1; --i) {
            dp = max(dp, stones[i] - dp);
        }

        return dp;
    }
};