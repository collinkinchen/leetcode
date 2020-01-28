#!/usr/bin/python3
class Solution:
    def plusOne(self, digits):
        if digits[len(digits)-1] == 9:
            
            digits[len(digits)-1] = 0
            i = 2
            while digits[len(digits)-i] == 9 and (len(digits)-i) != 0:
                print(digits)
                digits[len(digits)-i] = 0
                i = i + 1
            if len(digits)-i == 0 and digits[0] == 9:
                digits[0] = 1
                digits.append(0)
            else:
                digits[len(digits)-i] += 1
            if len(digits) == 1:
                digits.append(0)
        else:
            digits[len(digits)-1] += 1
        
        
        return digits
        


def main():
    print(obj.plusOne([1,2,3]))
    print(obj.plusOne([1,2,9]))
    print(obj.plusOne([9]))
    print(obj.plusOne([0]))
    print(obj.plusOne([9,9,9,9]))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    