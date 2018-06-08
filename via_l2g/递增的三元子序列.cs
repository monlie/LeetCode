public class Solution {
    public bool IncreasingTriplet(int[] nums) {
        int MAX = 10000000;
        int first = MAX;
        int second = MAX;
        int ext = MAX;
        foreach(int x in nums) {
            if (ext != MAX) {
                if (x > ext && x < second) {
                    first = ext;
                    second = x;
                    ext = MAX;
                    continue;
                }
            }
            if (first == MAX) first = x;
            if (second != MAX) {
                if (x > second) return true;
                if (x < second && x > first) second = x;
                if (x < first) ext = x;
            }
            else {
                if (x <= first) first = x;
                else second = x;
            }
        }
        return false;
    }
}
