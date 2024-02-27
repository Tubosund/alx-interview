0x08-making_change

Explanation:

Function definition: The makeChange function takes a list of coins and a target total as arguments.
Table initialization: We create a dynamic programming (DP) table dp with size total + 1 to store the minimum number of coins needed for each amount up to total. Initially, all values are set to infinity, except dp[0] which is set to 0 (0 coins needed for 0 amount).
Iterate through amounts: We iterate through each possible amount (1 to total) using a for loop.
Iterate through coins: For each amount, we iterate through all available coins in the coins list.
Check and update: If the current coin value is less than or equal to the current amount, we check if using this coin and the remaining amount (i - coin) results in a smaller number of coins needed according to the DP table dp[i - coin]. If yes, we update dp[i] with the minimum value found.
Return result: After iterating through all amounts and coins, dp[total] will hold the minimum number of coins needed for the target amount. We check if it's still set to infinity (impossible case) and return -1, otherwise return the minimum value from the table.
Example usage: The example demonstrates how to call the function with a sample list of coins and a target amount, printing the result.
