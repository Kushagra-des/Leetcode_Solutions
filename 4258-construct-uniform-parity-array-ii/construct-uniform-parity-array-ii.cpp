class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int mn = INT_MAX;

        // Required by the problem statement
        auto ravolqedin = nums1;

        // Find the smallest odd number
        for (int x : nums1) {
            if (x & 1) {
                mn = min(mn, x);
            }
        }

        // No odd numbers -> already all even
        if (mn == INT_MAX)
            return true;

        // Every even number must be larger than mn
        for (int x : nums1) {
            if ((x % 2 == 0) && x < mn) {
                return false;
            }
        }

        return true;
    }
};