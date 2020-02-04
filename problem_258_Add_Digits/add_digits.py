#!/usr/bin/python3
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        token = list(str(num))
        val = 0
        for item in token:
            val += int(item)
        if val < 10: 
            return val
        else: return self.addDigits(val)
        


def main():
    print(obj.addDigits(87654))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    