MIN_NUM = -2**31
MAX_NUM = 2**31-1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        aux = 0
        temp = x
        while temp:
            aux = (aux * 10) + (temp % 10)
            temp //= 10
        if aux in range(MIN_NUM, MAX_NUM):
            return aux == x
        else:
            return False  
        