import numpy as np

ALL = set(range(1, 10))


def find_cur(mat, last=None):
    if last:
        for i in range(last[0], 9):
            for j in range(9):
                if not mat[i, j]:
                    return i, j
    else:
        for i in range(9):
            for j in range(9):
                if not mat[i, j]:
                    return i, j


def poss_list(mat, pos):
    s = set()

    for value in mat[pos[0], :]:
        s.add(value)

    for value in mat[:, pos[1]]:
        s.add(value)

    sq_i, sq_j = pos[0]-pos[0] % 3, pos[1]-pos[1] % 3
    for value in mat[sq_i: sq_i+3, sq_j: sq_j+3].ravel():
        s.add(value)

    return list(ALL-s)


# 用于求解矩阵为mat的数独，返回不超过m个解组成的列表
def solve(mat_, m=1):
    solve_list = []

    def solve_iter(mat, n, last=None):
        if n:
            cur = find_cur(mat, last)
            nums = poss_list(mat, cur)
            for num in nums:
                new = mat.copy()
                new[cur] = num
                if len(solve_list) < m:   # 只要找到m个解就不继续寻找
                    solve_iter(new, n-1, cur)     # 下降
        else:
            solve_list.append(mat)

    n_ = len(mat_[mat_ == 0])
    solve_iter(mat_, n_)
    return solve_list


def str2mat(board):
    mat = np.zeros((9, 9), dtype=np.int8)
    zeros = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                mat[i, j] = board[i][j]
            else:
                zeros.append((i, j))
    return mat, zeros
    
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        ques, blanks = str2mat(board)
        solution = solve(ques)[0]
        for i, j in blanks:
            board[i][j] = str(solution[i, j])
        
