class Solution(object):

    # doesn't work when k is 0
    def findPairs_0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        table = []
        for i in nums:
            if (i+k) in table and i not in table:
                answer += 1
            if (i-k) in table and i not in table:
                answer += 1
            table.append(i)
        return answer

    def findPairs(self, nums, k):
        answer = 0
        if k < 0:
            return answer

        table = {}
        if k == 0:
            for i in nums:
                if table.get(i, 0) == 1:
                    answer += 1
                table[i] = table.get(i, 0) + 1
            return answer

        for i in nums:
            if table.get(i+k, 0) >= 1 and table.get(i, 0) == 0:
                answer += 1
            if table.get(i-k, 0) >= 1 and table.get(i, 0) == 0:
                answer += 1
            table[i] = table.get(i, 0) + 1
        return answer


def main():
    s = Solution()
    nums = [3, 1, 4, 1, 5]
    k = 2
    print s.findPairs(nums, k)

    nums = [1, 2, 3, 4, 5, 5, 4, 6, 5]
    k = 1
    print s.findPairs(nums, k)

if __name__ == "__main__":
    main()


