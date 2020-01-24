#!/usr/bin/python3
class Solution:
    def twoSum(self, nums, target):
        for i, val in enumerate(nums):
            for j, val2 in enumerate(nums):
                if val + val2 == target and i != j: return [i,j]


def main():
    nums = [2,7,11,15]
    target = 9
    print(obj.twoSum(nums,target))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    