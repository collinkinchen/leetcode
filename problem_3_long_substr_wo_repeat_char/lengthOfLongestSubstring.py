#!/usr/bin/python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        final_length = 0
        temp_list = []
        counter = 0
        string = list(s)
        done = False
        if len(string) < 2: return len(string)
        while not done:
    
            for i in range(index,len(string)):
                #print("index: %s" % index)
                #print(i)
                #print(index)
                if not string[i] in temp_list:
                    temp_list.append(string[i])
                    counter += 1
                else:
                    if counter > final_length:
                        final_length = counter
                    #print(temp_list)
                    temp_list.clear()
                    #print(temp_list)
                    counter = 0
                    index += 1
                    #print(index)
                    if (len(string)-index < final_length): done = True
                    break
            #counter = 0
            #temp_list.clear()
            #print("restarting for loop starting at index: %s" % index)
        return(final_length)


def main():
    s = "abcabcbb"
    print(obj.lengthOfLongestSubstring(s))

# Start program
if __name__ == "__main__":
    obj = Solution()
    main()
    