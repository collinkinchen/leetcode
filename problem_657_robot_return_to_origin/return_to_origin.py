#!/usr/bin/python3
class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0

        for move in moves:
            if move == 'U': y+=1
            if move == 'D': y-=1
            if move == 'R': x+=1
            if move == 'L': x-=1
        
        if x == 0 and y == 0: return True
        else: return False

def main():
    print(obj.judgeCircle("UDU"))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    