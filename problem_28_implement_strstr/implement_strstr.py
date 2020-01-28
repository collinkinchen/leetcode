#!/usr/bin/python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not needle in haystack: return -1
        else:
            temp = haystack.split(needle)
            return len(temp[0])
        


def main():
    print(obj.strStr("hello","ll"))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    