def push_up(tree, rt):
    tree[rt] = tree[rt<<1] + tree[rt<<1 | 1]
    

def build(tree, data, l, r, rt):
    if l == r:
        tree[rt] = data[l]
        return
    m = (l+r)>>1
    build(tree, data, l, m, rt<<1)
    build(tree, data, m+1, r, rt<<1 | 1)
    push_up(tree, rt)
    

def get_idx(begin, end, pos):
    l = begin
    r = end
    rt = 1
    while l < r:
        m = (l+r) >> 1
        if pos > m:
            l = m+1
            rt = rt<<1 | 1
        else:
            r = m
            rt = rt<<1
    return rt


def query_iter(tree, l, r, lq, rq, rt):
    if (lq <= l and rq >= r):
        return tree[rt]
    m = (l+r)>>1
    ans = 0
    if (m >= lq):
        ans += query_iter(tree, l, m, lq, rq, rt<<1)
    if (m < rq):
        ans += query_iter(tree, m+1, r, lq, rq, rt<<1 | 1)
    return ans


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums:
            nums = [0] + nums
            self.tree = [0] * (len(nums)*4)
            self.length = len(nums)-1
            build(self.tree, nums, 1, len(nums)-1, 1)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        rt = get_idx(1, self.length, i+1)
        self.tree[rt] = val
        p = rt >> 1
        while p:
            push_up(self.tree, p)
            p = p >> 1
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return query_iter(self.tree, 1, self.length, i+1, j+1, 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
