# give an array with unique values
# find all the three elements combinations from this array
# such that the sum of the first two element equals the third element

class Solution(object):
    def findTriplet(self, array):
        l = len(array)
        if l < 3:
            return
        array.sort()
        print(array)
        k = 2
        while k < l:
            i, j = (0, k-1)
            while i < j:
                sum = array[i] + array[j]
                if sum == array[k]:
                    print("{}, {}, {}".format(array[i], array[j], array[k]))
                    i += 1
                    j -= 1
                elif sum > array[k]:
                    j -= 1
                else:
                    i += 1
            k += 1


def main():
    s = Solution()
    array = [13, 1, 2, 3, 5, 7, 12,  8, 14, 9]
    s.findTriplet(array)

if __name__ == '__main__':
    main()
