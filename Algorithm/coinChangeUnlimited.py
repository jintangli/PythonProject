class Solution (object):

    # this one produces the same combinations for example [1,3] and [3, 1]
    # def makeChange(self, amount, coins, result):
    #     if(amount == 0):
    #         print result
    #     else:
    #         for coin in coins:
    #             if(amount < coin):
    #                 break
    #             else:
    #                 amount = amount - coin
    #                 result.append(coin)
    #                 self.makeChange(amount, coins, result)
    #                 result.pop()
    #                 amount = amount + coin

    def makeChange(self, amount, coins, result):
        if amount == 0 or len(coins):
            print result
        else:
            self.makeChange(amount, coins[1:], result)
            self.makeChange(amount-coins[0], coins[1:], result.push(coins[0]))







def main():
    s = Solution()
    coins = [1, 2, 3]
    amount = 4
    s.makeChange(amount, coins, [])


if __name__ == "__main__":
        main()









