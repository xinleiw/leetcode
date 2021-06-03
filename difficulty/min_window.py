import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        len_t = len(t)
        i = 0
        result = (0, float("inf"))
        for j, item in enumerate(s):
            if need[item] > 0:
                len_t -= 1
            need[item] -= 1
            if len_t == 0:
                while True:
                    item = s[i]
                    if need[item] == 0:
                        break
                    need[item] += 1
                    i += 1
                if j - i < result[1] - result[0]:
                    result = (i, j)
                need[s[i]] += 1
                len_t += 1
                i += 1
        return " " if result[1] > len(s) else s[result[0]: result[1]+1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow("adfasdfsafsagagassa", "ssg"))
