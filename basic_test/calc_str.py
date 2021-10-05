# Code 53.

# 给定一个字符串，逐个翻转字符串中的每个单词。
#==================
# 单词的构成：无空格字母构成一个单词，有些单词末尾会带有标点符号
# 输入字符串是否包括前导或者尾随空格？
# 可以包括，但是反转后的字符不能包括

# 如何处理两个单词间的多个空格？
# 在反转字符串中间空格减少到只含一个

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here