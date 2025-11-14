def knapSack(W, wt, val, n):
    # Initialize a 2D DP table with (n+1) rows and (W+1) columns, filled with 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):  # Loop through items (1-based index)
        for w in range(W + 1):  # Loop through weights
            if wt[i - 1] <= w:  # If current item weight can be included
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:  # Else, exclude the item
                dp[i][w] = dp[i - 1][w]

    # The maximum value is found in dp[n][W]
    max_value = dp[n][W]

    # Traceback to find the items included in the optimal solution
    w = W
    selected_items = []
    for i in range(n, 0, -1):
        # Check if this item is included in the optimal solution
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Store the item index (0-based)
            w -= wt[i - 1]  # Reduce the remaining weight

    # Print results
    print("Maximum value:", max_value)
    print("Items included (0-based index):", selected_items[::-1])

# Example usage
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
knapSack(W, wt, val, n)
