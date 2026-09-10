prices = list(map(int, input("Enter prices: ").split()))

min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit

print("Maximum Profit:", max_profit)