def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0

    n = len(prices)
    # Khá»i táº¡o cÃ¡c máº£ng lÆ°u trá»¯ lá»£i nhuáº­n tá»i Äa cÃ³ thá» Äáº¡t ÄÆ°á»£c
    max_profit_left = [0] * n
    max_profit_right = [0] * n

    # TÃ­nh lá»£i nhuáº­n tá»i Äa tá»« trÃ¡i sang pháº£i
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit_left[i] = max(max_profit_left[i - 1], prices[i] - min_price)

    # TÃ­nh lá»£i nhuáº­n tá»i Äa tá»« pháº£i sang trÃ¡i
    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit_right[i] = max(max_profit_right[i + 1], max_price - prices[i])

    # TÃ­nh tá»ng lá»£i nhuáº­n tá»i Äa tá»« hai lÆ°á»£t giao dá»ch
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, max_profit_left[i] + max_profit_right[i])

    return max_profit

# VÃ­ dá»¥
n = int(input())
stock_prices = [int(x) for x in input().split()]
result = maxProfit(stock_prices)
print(result)