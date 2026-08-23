class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();

        int s1 = 0, s2 = 0;
        int c1 = 0, c2 = 0;

        for (int i = 0; i < n / 2; i++) {
            if (num[i] == '?')
                c1++;
            else
                s1 += num[i] - '0';
        }

        for (int i = n / 2; i < n; i++) {
            if (num[i] == '?')
                c2++;
            else
                s2 += num[i] - '0';
        }

        return (c1 + c2) % 2 == 1 ||
               (s1 - s2) != 9 * (c2 - c1) / 2;
    }
};