#!/usr/bin/python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        items = list(s)
        if len(items)%2 != 0: return False
        for item in items:
            if item == '[' or item == '{' or item == '(':
                stack.append(item)
            if item == ']' or item == '}' or item == ')':
                if not stack: return False
                else:
                    if item == ']' and stack[-1] == '[': 
                        stack.pop()
                    if item == '}' and stack[-1] == '{': 
                        stack.pop()
                    if item == ')' and stack[-1] == '(': 
                        stack.pop()
        if not stack: return True
        else: return False


def main():
    s = '(())()'
    print(obj.isValid(s))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    