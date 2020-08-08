'''编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ''
        for i in zip(*strs):  # zip的使用
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans
