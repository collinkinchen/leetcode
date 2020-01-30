#!/usr/bin/python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        if n % 2 != 0: return False
        
        powlist = []
        for i in range(0,64): powlist.append(pow(2,i))
        if n in powlist: return True
        else: return False
        


def main():
    print(obj.isPowerOfTwo(16))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    