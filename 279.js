/**
 * @param {number} n
 * @return {number}
 */
 // 我丢这题js都能ac，python给我tle是几个意思？
var numSquares = function(n) {
    var lis = new Array(n+1);
    var k, m, l;
    lis[0] = 0;
    for (var i = 1; i < n+1; i++) {
        k = Math.floor(Math.sqrt(i));
        if (k*k == i) {
            lis[i] = 1;
            continue;
        }
        m = lis[i-1];
        for (var j = 1; j < k; j++) {
            l = lis[i-(j+1)*(j+1)];
            if (l < m) m = l;
        }
        lis[i] = m + 1;
    }
    return lis[n];
};