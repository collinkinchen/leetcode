#!/usr/bin/python3
class Solution:
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for item in A:
            if item%2 == 0: even.append(item)
            else: odd.append(item)
        return even + odd
        


def main():
    print(obj.sortArrayByParity([1,3,5,7,9,2,4,6,8]))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    