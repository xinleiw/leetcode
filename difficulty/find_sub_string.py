from collections import defaultdict


class Solution(object):

    def findSubstring(self, s, words):
        """
        :param s:
        :param words:
        :return:
        """
        need = defaultdict(int)
        word_len = 0
        for word in words:
            need[word] += 1
            word_len = len(word)
        words_len = len(words)
        if len(s) < words_len * word_len:
            return []
        start = 0
        res = []
        win_size = words_len * word_len
        while start < len(s) - win_size + 1:
            temp = need.copy()
            for i in range(start, start + win_size, word_len):
                part = s[i: i+word_len]
                if part not in temp:
                    break
                else:
                    temp[part] -= 1
                    if temp[part] < 0:
                        break
            else:
                res.append(start)
            start += 1
        return res
