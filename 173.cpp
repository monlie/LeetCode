/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    stack<TreeNode *> s;
    TreeNode *pr;
    BSTIterator(TreeNode *root) {
        while (root) {
            //cout << root->val << endl;
            s.push(root);
            root = root->left;
        }
        pr = root;
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty() || pr;
    }

    /** @return the next smallest number */
    int next() {
        int v;
        while (pr) {
            s.push(pr);
            pr = pr->left;
        }
        pr = s.top();
        s.pop();
        v = pr->val;
        pr = pr->right;
        return v;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */