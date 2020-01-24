#!/usr/bin/python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        palStr = str(x)
        left = 0
        right = len(palStr) -1
        while left < right:
            if not palStr[left] == palStr[right]:
                return False
            left = left + 1
            right = right - 1
        return True


def main():
    # x = 123321
    x = 12332
    print(obj.isPalindrome(x))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    