import heapq


class Word(object):
    
    def __init__(self, word, times):
        self.word = word
        self.times = times
        
    def __lt__(self, other):
        return self.word > other.word if self.times == other.times else self.times < other.times
        
        
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        heap = []
        
        for word in words:
            if word in dic:
                heap[dic[word]].times += 1
            else:
                heap.append(Word(word, 1))
                dic[word] = len(heap)-1
                
        result = heapq.nlargest(k, heap)
        
        return [i.word for i in result]