import heapq


class Pair(object):
    
    def __init__(self, i, j):
        self.tpl = (i, j)
        
    def __lt__(self, a):
        return self.tpl[1] < a.tpl[1]

    
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        l = []
        for key, val in counter.items():
            l.append(Pair(key, val))
        heapq._heapify_max(l)
        r = ''
        while l:
            key, count = heapq._heappop_max(l).tpl
            r += key*count
        return r
