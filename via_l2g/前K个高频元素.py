import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        return [i[0] for i in heapq.nlargest(k, dic.items(), key=lambda x: x[1])]
        
        
