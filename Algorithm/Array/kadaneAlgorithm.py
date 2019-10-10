# Given an array arr of N integers. Find the contiguous sub-array with maximum sum


class Solution(object):

    def __init__(self, array):
        self.data = array

    def findSubArray(self):
        print "enter findSubArray"
        index = 1
        sum, max = (self.data[0], self.data[0])
        start, tempStart = (0, 0)
        end, tempEnd = (0, 0)

        arrayLen = len(self.data)
        while index < arrayLen:
            if sum < 0:
                sum = self.data[index]
                if sum >= max:
                    max = sum
                    start, tempStart, end, tempEnd = (index, index, index, index)
                else:
                    tempStart, tempEnd = (index, index)
            else:
                sum = sum + self.data[index]
                if sum >= max:
                    max = sum
                    start = tempStart
                    tempEnd = index
                    end = tempEnd
                else:
                    tempEnd = index
            print "index is {}, sum is {}, [start = {}, end = {}]".format(index, sum, start, end)
            index += 1

        return [start, end]


def main():
    array = [-1, -2, 3, -9, 6, 5, 4, -11]
    solution = Solution(array)
    result = solution.findSubArray()
    print result
    print "****************************************************"
    array = [-1, -2, 3, -9, 6, 5, 4, -11, 10]
    solution.data = array
    result = solution.findSubArray()
    print result
    print "****************************************************"
    array = [-1, -2, 3, -9, 6, 5, 4, -11, 19]
    solution.data = array
    result = solution.findSubArray()
    print result
    print "****************************************************"
    array = [-1]
    solution.data = array
    result = solution.findSubArray()
    print result
    print "****************************************************"
    array = [-1, -2, -3, -4, -5]
    solution.data = array
    result = solution.findSubArray()
    print result



if __name__ == "__main__":
    main()


