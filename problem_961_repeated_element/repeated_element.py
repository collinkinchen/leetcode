#!/usr/bin/python3
class Solution:
    def repeatedNTimes(self, A):
        count = len(A)/2
        for item in A:
            if count == A.count(item): return item
        


def main():
    print(obj.repeatedNTimes([1,2,3,3]))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    