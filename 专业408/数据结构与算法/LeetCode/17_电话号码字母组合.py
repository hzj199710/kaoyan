from typing import List

class Solution:
    charac_list = ["abc", "def", "ghi", 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def func_t(self, res, pre, digits):
        if len(digits) <=0:
            return
        elif len(digits) == 1:
            num = int(digits[0])
            for ele in self.charac_list[num-2]:
                res.append(pre + ele)
        else:
            num = int(digits[0])
            for ele in self.charac_list[num-2]:
                self.func_t(res, pre+ele, digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.func_t(res, "", digits)
        return res
