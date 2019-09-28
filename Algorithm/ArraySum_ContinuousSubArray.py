class Solution(object):

    def findSubArray(self, array, sum):
        i, j, k = (0, 0, len(array))
        temp = array[i]
        while i<=j<k:
            if(temp == sum):
                print(str(i) + " " + str(j) + ",")
                temp = temp - array[i]
                i += 1
                j += 1
                if j < k:
                    temp = temp + array[j]
                else:
                    return
            elif temp < sum and j < k :
                j += 1
                temp = temp + array[j]

            elif temp > sum and i < j:
                temp = temp - array[i]
                i += 1
            else:
                return










def main():
    s = Solution()
    array = [3, 5, 7, 12, 11, 8, 9, 7,  1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
    sum = 12
    s.findSubArray(array, sum)



if __name__ == "__main__":
    main()