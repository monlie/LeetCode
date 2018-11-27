def rcr_sum(l, s):
    count = []
    if l and s > 0:
        if l[0] == s:
            count.append([s])
        count += rcr_sum(l[1:], s) + [i + [l[0]] for i in rcr_sum(l, s - l[0])]
    return count
        

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return rcr_sum(candidates, target)
        