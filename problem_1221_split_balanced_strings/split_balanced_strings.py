#!/usr/bin/python3
class Solution:

    def balancedStringSplit(self, s: str) -> int:
        finalCount = 0

        stringlength = len(s)
        lLength = 0
        rLength = 0
        for i in range(stringlength):
            if s[i] == 'L':
                lLength += 1
            else:
                rLength += 1

            if lLength == rLength:
                finalCount += 1
                lLength = 0
                rLength = 0

        return finalCount        


def main():
   print(obj.balancedStringSplit('LRLLRRLRLRLLRR'))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    