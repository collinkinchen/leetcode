#!/usr/bin/python3
'''
Given an array and an int find if there are 2 values in the array that are <= k distance apart
- go through array indicies
- go through array for k more idicies
- if you run into the same number then return true
- if you go through the whole array then return true

possible optimizations:
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        if len(set(nums)) == len(nums): return False
        for index in range(len(nums)):
            temp = 1
            try:
                while temp <= k:
                    if nums[index] == nums[index+temp]: return True
                    else: temp += 1
            except:
                pass
        return False


def main():
    print(obj.containsNearbyDuplicate([1,2,3,1,5],3))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    
