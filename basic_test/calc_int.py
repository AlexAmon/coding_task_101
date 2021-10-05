# Code 37.

# 反转一个只有3位数的整数。
# 你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000。


class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        number = 123
        num_i = 0
        revnum = 0
        for i in range(3):
            num_i = number // (10**(i)) % 10
            revnum = (10**(2-i)) * num_i 
        print(revnum)
        
            
    
