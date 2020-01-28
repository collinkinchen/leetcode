#!/usr/bin/python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        # print("-%s-" % s)
        s = s.rstrip()
        # print("-%s-" % s)
        temp = s.split(" ")
        return len(temp[-1])
        


def main():
    print(obj.lengthOfLastWord("this is a test string with a long last word bazingaringodingo"))
    print(obj.lengthOfLastWord("this is a test string with a short last word hi"))
    print(obj.lengthOfLastWord(""))
    print(obj.lengthOfLastWord("hello"))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    