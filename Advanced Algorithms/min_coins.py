def min_coins(amount, coins):
    # Initialize count to store the number of coins
    count = 0

    # Iterate through the coins in descending order of their denominations
    for i in range(len(coins)):
        # Iterate through the coins from the first to the second-to-last
        for j in range(len(coins) - 1):
            # Swap adjacent coins if the current coin is greater than the next one
            if coins[j] < coins[j + 1]:
                coins[j], coins[j + 1] = coins[j + 1], coins[j]

    # Iterate through the coins in descending order
    for coin in coins:
        # Calculate how many coins of this denomination can be used
        num_coins = amount // coin
        # Update the amount remaining after using these coins
        amount -= num_coins * coin
        # Update the count of total coins used
        count += num_coins

    return count


# Sample Input
amount = 63
coins = [1, 5, 10, 25]

# Sample Output
print(min_coins(amount, coins))  # Output: 6