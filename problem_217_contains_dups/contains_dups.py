#!/usr/bin/python3
class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) < len(nums): 
            return True
        else: return False
        


def main():
    print(obj.containsDuplicate([2,1,2,5]))
    print(obj.containsDuplicate([2]))
    print(obj.containsDuplicate([2,2]))
    print(obj.containsDuplicate([1,2,3,4,5,6,7,8,9,1000,1001,2]))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    