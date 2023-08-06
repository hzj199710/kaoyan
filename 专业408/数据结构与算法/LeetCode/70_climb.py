# 分析：要到达第n层，可以从第n-1层走1步上去，也可以从第n-2层走2步上去
# 存在递归条件，f(n) = f(n-1) + f(n-2)
# 为避免重复计算的情况，使用字典记录所有的项

class Solution:
    def climbStairs(self, n: int) -> int:
        climb_list = {0:1, 1:2}
        if n <= 2:
            return climb_list[n-1]
        else:
            for i in range(2, n):
                climb_list[i] = climb_list[i-2] + climb_list[i-1]
        return climb_list[n-1]