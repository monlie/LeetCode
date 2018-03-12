// cpp过了python没过...
class Solution {
public:
    int nthUglyNumber(int n) {
        long lis[n], m, su;
        int num[3] = { 2, 3, 5 };
        int idx;
        lis[0] = 1;
        for (int i = 1; i < n; i++) {
            m = 2 * lis[i-1];
            for (int j = 0; j < i; j++) {
                idx = i-j-1;
                if (5 * lis[idx] <= lis[i-1]) break;
                for (int k = 0; k < 3; k++) {
                    su = num[k] * lis[idx];
                    if (su >= m) break;
                    if (su > lis[i-1]) m = su;
                }
            }
            lis[i] = m;
        }
        return lis[n-1];
    }
};