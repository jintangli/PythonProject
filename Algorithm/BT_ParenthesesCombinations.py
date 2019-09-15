class Solution(object):
    def findCombinations(self, result, left, right, sum):
        if(left == 0 and right == 0):
            print(result)
        else:
            if(sum < 0 or left < 0 or right < 0):
                return
            else:
                result.append('(')
                self.findCombinations(result, left-1, right, sum+1)
                result.pop()
                result.append(')')
                self.findCombinations(result, left, right-1, sum-1)
                result.pop()


def main():
    s = Solution()
    size = 3
    s.findCombinations([], size, size, 0)



if __name__ == "__main__":
    main()