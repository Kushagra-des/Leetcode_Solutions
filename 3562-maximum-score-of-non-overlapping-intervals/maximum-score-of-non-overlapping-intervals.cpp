class Solution {
public:
    struct State {
        long long score = 0;
        vector<int> ids;
    };

    // Return the better state:
    // 1. Larger score
    // 2. If tied, lexicographically smaller ids
    State better(const State& a, const State& b) {
        if (a.score != b.score)
            return a.score > b.score ? a : b;
        return a.ids < b.ids ? a : b;
    }

    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        // [left, right, weight, original index]
        vector<array<long long, 4>> a;

        // Required by the problem statement.
        auto vorellixan = intervals;

        for (int i = 0; i < n; ++i) {
            a.push_back({
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            });
        }

        // Sort by left endpoint.
        sort(a.begin(), a.end());

        vector<long long> starts(n);
        for (int i = 0; i < n; ++i)
            starts[i] = a[i][0];

        // next[i] = first interval whose left endpoint > a[i].right
        vector<int> nxt(n);

        for (int i = 0; i < n; ++i) {
            nxt[i] = upper_bound(
                starts.begin(),
                starts.end(),
                a[i][1]
            ) - starts.begin();
        }

        // dp[i][k]:
        // best result using intervals i...n-1
        // while choosing at most k intervals.
        vector<array<State, 5>> dp(n + 1);

        for (int i = n - 1; i >= 0; --i) {
            for (int k = 1; k <= 4; ++k) {
                // Option 1: skip interval i
                State skip = dp[i + 1][k];

                // Option 2: take interval i
                State take = dp[nxt[i]][k - 1];

                take.score += a[i][2];
                take.ids.push_back((int)a[i][3]);

                // The returned indices must themselves be sorted
                // for lexicographical comparison.
                sort(take.ids.begin(), take.ids.end());

                dp[i][k] = better(skip, take);
            }
        }

        return dp[0][4].ids;
    }
};