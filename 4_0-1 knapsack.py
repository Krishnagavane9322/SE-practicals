def knapsack_01(num_items, values, weights, max_weight):
    # Initialize DP table with 0 values
    dp = [[0] * (max_weight + 1) for _ in range(num_items + 1)]

    # Fill DP table
    for item in range(1, num_items + 1):
        for weight in range(max_weight + 1):
            # If item is too heavy, inherit the value from above
            if weights[item - 1] > weight:
                dp[item][weight] = dp[item - 1][weight]
            else:
                # Otherwise, choose max of including or excluding the item
                dp[item][weight] = max(dp[item - 1][weight], 
                                       dp[item - 1][weight - weights[item - 1]] + values[item - 1])

    # Backtrack to find items included in the optimal solution
    chosen_items = []
    weight = max_weight
    for item in range(num_items, 0, -1):
        # Check if this item was included by comparing values in dp table
        if dp[item][weight] != dp[item - 1][weight]:
            chosen_items.append(item - 1)  # Add this item's index
            weight -= weights[item - 1]    # Reduce the weight by this item's weight

    # Return max value and the chosen items list (reversed for correct order)
    return dp[num_items][max_weight], list(reversed(chosen_items))

# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_weight = 50

    max_value, chosen_items = knapsack_01(len(values), values, weights, max_weight)
    print("Maximum value:", max_value)
    print("Chosen items:", chosen_items)
