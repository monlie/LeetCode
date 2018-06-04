public class Solution {
    public int LengthOfLIS(int[] nums) {
        if (nums.Length == 0) return 0;
        int [] lim = new int[nums.Length];
        int m, cur;
        lim[0] = 1;
        cur = 1;
        for (int i = 1; i < nums.Length; i++) {
            m = 0;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i] && lim[j] > m) {
                    m = lim[j];
                }
            }
            lim[i] = m + 1;
            if (lim[i] > cur) cur = lim[i];
        }
        return cur;
    }
}
