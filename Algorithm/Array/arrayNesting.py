class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dic = {i: 0 for i in range(size)}
        r = 0
        for i in range(size):
            r = max(r, self.count(nums, dic, i))
        return r

    def count(self, nums, dic, i):
        count = 1
        j = nums[i]
        while i != j and not dic[j]:
            count += 1
            j = nums[j]

        if i == j:
            dic[i] = count
            return count
        dic[i] = dic[j]
        return dic[i]

def main():
    s = Solution()
    nums = [5,4,0,3,1,6,2]
    dic = {i:0 for i in range(len(nums))}
    r = s.arrayNesting(nums)
    print dic
    print r
    # for i in range(len(nums)):
    #    r = s.count(nums, dic, i)
    #    print "i is {}, count is {}".format(i, r)
    # print s.count(nums, dic, 5)


if __name__ == "__main__":
    main()
