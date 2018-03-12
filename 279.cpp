class Solution {
public:
    int numSquares(int n) {
        int lis[n+1];
        int k, m, l;
        lis[0] = 0;
        for (int i = 1; i < n+1; i++){
            k = floor(sqrt(i));
            if (k*k == i) {
                lis[i] = 1;
                continue;
            }
            m = lis[i-1];
            for (int j = 1; j < k; j++) {
                l = lis[i-(j+1)*(j+1)];
                if (l < m) m = l;
            }
            lis[i] = 1 + m;
        }
        return lis[n];
    }
};