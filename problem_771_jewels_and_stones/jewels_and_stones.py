#!/usr/bin/python3
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = list(J)
        token = list(S)
        out = 0
        for item in token:
            if item in jewels: 
                out = out + 1
        return out
        


def main():
    print(obj.numJewelsInStones("aA","aaAHHHHH"))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    