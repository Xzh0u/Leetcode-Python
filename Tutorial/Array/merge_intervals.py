'''给出一个区间的集合，请合并所有重叠的区间。
e.g.
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
'''
from typing import List


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         li = []
#         i = 0
#         if len(intervals) <= 1: return intervals
#         while i < len(intervals) - 1:
#             if intervals[i][1] >= intervals[i + 1][0]:
#                 if intervals[i][1] <= intervals[i + 1][1]:
#                     li.append([intervals[i][0], intervals[i + 1][1]])
#                 else:
#                     li.append([intervals[i][0], intervals[i][1]])
#                 i = i + 1
#             else:
#                 li.append(intervals[i])
#                 li.append(intervals[i + 1])
#             i = i + 1
#         return li
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][0] = min(intervals[i - 1][0], intervals[i][0])
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i = i + 1
        return intervals


if __name__ == "__main__":
    a = Solution()
    b = a.merge([[1, 4], [2, 3]])
    print(b)