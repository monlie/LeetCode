class Solution {
public:

    int possMin(int a, int b) {
        if (a == -1) return b;
        if (b == -1 && a != -1) return a + 1;
        return min<int>(a + 1, b);
    }
    
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        
        int a[amount + 1][coins.size()];
        int x, y, m;
        
        for (int i = 0; i < coins.size(); i++) {
            a[0][i] = 0;
        }
        
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                x = (i - coins[j] < 0 || j < 0)? -1 : a[i - coins[j]][j];
                y = (i < 0 || j - 1 < 0)? -1 : a[i][j - 1];
                a[i][j] = possMin(x, y);
            }
        }
        
        m = -1;
        
        for (int i = 0; i < coins.size(); i++) {
            if (a[amount][i] != -1 && (a[amount][i] < m || m == -1)) {
                m = a[amount][i];
            }
        }
        return m;
    }
};