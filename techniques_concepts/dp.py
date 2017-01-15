n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]

coins = sorted(coins, reverse=True)
# sort coins to use from greater coins

tb = {}
# tb memorises the output of dp(c,n)
# since we don't have to record the whole array of the coins,
# you put a tuple of (the number of the remaining coins, the target value)

def dp(coins, n):
    # coins = the usable coins
    # n = the target value
    # dp(c,n) outputs the number of patterns
    l = len(coins)
    if coins == [] or n < 0:
        return 0
    elif n == 0:
        return 1
    elif not (l, n) in tb:
        res = 0
        for idx, coin in enumerate(coins):
            if n - coin >= 0:
                # you only use coins less than or equal to
                # the coin you have just used
                res += dp(coins[idx:], n - coin)
        tb[(l, n)] = res
    return tb[(l, n)]

print(dp(coins, n))
