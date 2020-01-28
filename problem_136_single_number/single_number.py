#!/usr/bin/python3
class Solution:
    def singleNumber(self, nums) -> int:
        temp = []
        for item in nums:
            if item not in temp: temp.append(item)
            else: temp.remove(item)
        if not temp: return 0
        else: return temp[0]
        


def main():
    print(obj.singleNumber([2,2,1]))
    print(obj.singleNumber([2,2,4,3,3]))
    print(obj.singleNumber([2,2,6,3,7,3,6]))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    