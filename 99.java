/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private ArrayList<TreeNode> lis = new ArrayList<>();
    private void dfs(TreeNode root) {
        if (root != null) {
            dfs(root.left);
            lis.add(root);
            dfs(root.right);
        }
    }
    public void recoverTree(TreeNode root) {
        dfs(root);
        TreeNode last = lis.get(0);
        ArrayList<TreeNode> errorList = new ArrayList<>();
        int count = 0;
        for (TreeNode curPtr: lis) {
            if (curPtr.val < last.val) {
                if (count == 0) {
                    errorList.add(last);
                    errorList.add(curPtr);
                    count++;
                }
                else if (count == 1) {
                    errorList.set(1, curPtr);
                    break;
                }
            }
            last = curPtr;
        }
        int tmp = errorList.get(0).val;
        errorList.get(0).val = errorList.get(1).val;
        errorList.get(1).val = tmp;
    }
}
