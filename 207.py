class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [0] * numCourses
        graph = [[[], []] for _ in range(numCourses)]
        
        for v, u in prerequisites:
            in_degree[v] += 1
            graph[u][1].append(v)
            graph[v][0].append(u)
            
        stack = []
        s = []
        for n, i  in enumerate(in_degree):
            if not i:
                stack.append(n)
        while stack:
            node = stack.pop()
            s.append(node)
            for u in graph[node][1]:
                in_degree[u] -= 1
                if not in_degree[u]:
                    stack.append(u)
        return len(s) == numCourses
            
