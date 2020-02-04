#!/usr/bin/python3
class Solution:
    def defangIPaddr(self, address):
        address = address.replace(".","[.]")
        return address
        


def main():
    print(obj.defangIPaddr("1.2.3.4"))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    