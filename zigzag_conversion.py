from lc import *

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        middle = numRows - 2
        lines = [""] * numRows
        for (i, c) in enumerate(s):
            x = i%(numRows+middle)
            if x < numRows:
                lines[x] += c
            else:
                lines[middle+numRows-x] += c
        return "".join(lines)
        