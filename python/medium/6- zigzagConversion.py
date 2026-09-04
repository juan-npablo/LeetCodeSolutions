class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]
        i, ptr = 0, 0
        while ptr < len(s):
            for i in range(numRows):
                matrix[i].append(s[ptr] if ptr < len(s) else None)
                ptr += 1
            while i - 1 > 0:
                i -= 1
                matrix[i].append(s[ptr] if ptr < len(s) else None)
                ptr += 1
        solution = ''
        for lista in matrix:
            solution += ''.join([x for x in lista if x is not None])
        return solution

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]
        current_row = 0
        going_down = True
        for ptr in s:
            if numRows == 1:
                return s

            print(current_row)
            matrix[current_row].append(ptr)
            if going_down:
                current_row += 1
            else:
                current_row -= 1
            if (current_row == 0 or current_row == numRows-1):
                going_down = not(going_down)
        solution = ''
        for lista in matrix:
            solution += ''.join([x for x in lista if x is not None])
        return solution