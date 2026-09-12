MAX_NUM = 2**31-1
MIN_NUM = -2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        temp = ""
        for letter in s:
            if letter.isalpha() or letter == ".":
                    break
            elif letter.isnumeric():
                result = result * 10 + int(letter)
                temp += letter
            elif letter == "-":
                if temp == "" and temp != "-" and temp != "+":
                    sign = -1
                    temp += letter
                else:
                    break
            elif letter == "+":
                if temp == "" and temp != "-" and temp != "+":
                    sign = 1
                    temp += letter
                else:
                    break
            elif letter == " " and temp:
                break

        result = result * sign
        if result < MIN_NUM:
            return MIN_NUM
        if result > MAX_NUM:
            return MAX_NUM
        return result