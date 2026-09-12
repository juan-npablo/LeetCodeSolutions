MAX_NUM = 2147483647
MIN_NUM = -2147483648

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            inv_numb = str(x)
            inv_numb = inv_numb[::-1]
        else:
            x *= -1
            inv_numb = str(x)
            inv_numb = inv_numb[::-1]
            inv_numb = "-"+inv_numb
        return int(inv_numb) if int(inv_numb) < MAX_NUM and int(inv_numb) > MIN_NUM else 0


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        inv_numb = ""

        while x:
            temp = x % 10
            inv_numb = inv_numb + str(temp)
            x = x//10

        result = int(inv_numb) * sign
        return result if result in range(-2**31, 2**31-1) else 0