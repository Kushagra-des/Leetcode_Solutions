class Solution {
public:
    int ans = 0;

    pair<int, int> dfs(TreeNode* root) {
        if (!root)
            return {0, 0};  // {sum, count}

        auto [leftSum, leftCount] = dfs(root->left);
        auto [rightSum, rightCount] = dfs(root->right);

        int sum = leftSum + rightSum + root->val;
        int count = leftCount + rightCount + 1;

        if (root->val == sum / count)
            ans++;

        return {sum, count};
    }

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};