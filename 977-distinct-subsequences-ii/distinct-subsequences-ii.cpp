class Solution {
public:
    int distinctSubseqII(string s) {
        const long long MOD = 1e9 + 7;

        vector<long long> dp(s.size() + 1);
        vector<int> last(26, -1);

        dp[0] = 1; // empty subsequence

        for (int i = 1; i <= s.size(); i++) {
            int c = s[i - 1] - 'a';

            dp[i] = (2 * dp[i - 1]) % MOD;

            if (last[c] != -1) {
                dp[i] = (dp[i] - dp[last[c]] + MOD) % MOD;
            }

            last[c] = i - 1;
        }

        // Remove empty subsequence
        return (dp[s.size()] - 1 + MOD) % MOD;
    }
};