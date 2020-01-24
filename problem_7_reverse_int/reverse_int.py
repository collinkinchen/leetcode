#!/usr/bin/python3
class Solution:
    def reverse(self, x: int) -> int:
        final = ""
        if str(x)[0] == "-": 
            left = 1
            final = final + "-"
        else: left = 0
        right = len(str(x)) -1
        while not right == (left -1):
            final = final + str(x)[right]
            right = right -1
        if (int(final) > 2147483648 or int(final) < -2147483648): 
            return 0 
        else: return int(final)


def main():
    # x = 123
    x = 987654321
    print(obj.reverse(x))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    