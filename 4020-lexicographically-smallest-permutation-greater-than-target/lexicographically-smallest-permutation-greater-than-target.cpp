class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();

        vector<int> cnt(26);
        for (char c : s)
            cnt[c - 'a']++;

        string prefix;

        // First try to match target exactly as far as possible.
        for (int i = 0; i < n; i++) {
            int x = target[i] - 'a';

            if (cnt[x] > 0) {
                prefix += target[i];
                cnt[x]--;
                continue;
            }

            // Cannot match target[i].
            // Try making this position larger.
            for (int c = x + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    string ans = prefix;
                    ans += char('a' + c);
                    cnt[c]--;

                    for (int k = 0; k < 26; k++)
                        ans += string(cnt[k], char('a' + k));

                    return ans;
                }
            }

            // Can't increase here, so backtrack.
            break;
        }

        // Backtrack through positions that were matched exactly.
        for (int i = (int)prefix.size() - 1; i >= 0; i--) {
            // Return the character used at this position to the pool.
            cnt[prefix[i] - 'a']++;

            int x = target[i] - 'a';

            // Find smallest available character > target[i].
            for (int c = x + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    string ans = prefix.substr(0, i);
                    ans += char('a' + c);
                    cnt[c]--;

                    // Since ans is already > target,
                    // minimize the suffix.
                    for (int k = 0; k < 26; k++)
                        ans += string(cnt[k], char('a' + k));

                    return ans;
                }
            }
        }

        return "";
    }
};