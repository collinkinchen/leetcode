#!/usr/bin/python3
class Solution:
    def searchInsert(self, nums, target: int) -> int:
            if target in nums:
                return nums.index(target)
            else:
                if target > nums[-1]: return len(nums)
                for i,value in enumerate(nums):
                    if target < value:
                        return (i)
                #i = len(nums)-1
                #while target <= nums[i]:
                #    i -= 1
                #return i+1
        


def main():
    print(obj.searchInsert([1,3,5,6],5))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    