class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        preTime, poisonTime = -1, -1
        answer = 0
        for newTime in timeSeries:
            if newTime >= poisonTime:
                answer += duration
            if newTime < poisonTime:
                answer = answer + (newTime - preTime)
            poisonTime = newTime + duration
            preTime = newTime
        return answer

def main():
    s = Solution()
    timeSeries = [1,4]
    duration = 2
    print s.findPoisonedDuration(timeSeries, duration)
    timeSeries = [1,2]
    duration = 2
    print s.findPoisonedDuration(timeSeries, duration)
    timeSeries = [1,2,3,4,5,6,7,8,9]
    duration = 1
    print s.findPoisonedDuration(timeSeries, duration)

if __name__ == "__main__":
    main()