class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        lis = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if stack:
                if temp <= temperatures[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and temp > temperatures[stack[-1]]:
                        j = stack.pop()
                        lis[j] = i - j
                    stack.append(i)
            else:
                stack.append(i)
                
        return lis