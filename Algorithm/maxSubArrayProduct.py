class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = dict()
        length = len(nums)
        r = nums[0]
        for i in range(length):
            table[i] = dict()
            for j in range(i, length):
                if i == j:
                    table[i][j] = nums[i]

                else:
                    table[i][j] = nums[j]*table[i][j-1]

                r = max(r, table[i][j])
        return r



def main():
    nums = [2, 3, -2, 4, -3, -2, -3, 4, -2]
    s = Solution()
    r = s.maxProduct(nums)
    print r

if __name__ == "__main__":
    main()
