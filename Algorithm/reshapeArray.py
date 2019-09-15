class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        oldr = len(nums)
        oldc = len(nums[0])
        oldsize = oldr * oldc
        newsize = r * c
        if (oldr*oldc != r*c):
            return nums
        newnums = list()
        for i in range(r):
            row = list()
            for j in range(c):
                k = i*c+j
                # print "{}({},{})".format(k, (k)/oldc, (k)%oldc)
                row.append(nums[k/oldc][k%oldc])
            newnums.append(row)


        return newnums

def main():
    s = Solution()
    print s.matrixReshape([[1,2,3,4,5,6], [7,8,9,10,11,12]], 1, 13)
if __name__ == "__main__":
    main()