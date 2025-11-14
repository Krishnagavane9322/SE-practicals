import sys

def fibonacci_iter(n):
    if n < 0:
        return -1, 1, []
    if n == 0:
        return 0, 1, [0]
    if n == 1:
        return 1, 1, [0, 1]
    
    steps = 0
    a = 0
    b = 1
    series = [a, b]
    
    for i in range(2, n + 1):
        c = a + b
        series.append(c)
        a = b
        b = c
        steps += 1
    
    return series[-1], steps + 1, series

def fibonacci_recur(n, memo=None, series_cache=None):
    if memo is None:
        memo = {}
    if series_cache is None:
        series_cache = {}
    
    if n < 0:
        return -1, 1, []
    if n == 0:
        return 0, 1, [0]
    if n == 1:
        return 1, 1, [0, 1]
    
    # Check memoization cache
    if n in memo:
        return memo[n][0], memo[n][1], series_cache[n]
    
    fib1, steps1, series1 = fibonacci_recur(n - 1, memo, series_cache)
    fib2, steps2, series2 = fibonacci_recur(n - 2, memo, series_cache)
    
    # Calculate result
    result = fib1 + fib2
    total_steps = steps1 + steps2 + 1
    
    # Build series: use series from n-1 and append the new result
    series = series1.copy()
    if result not in series:
        series.append(result)
    
    # Cache the result
    memo[n] = (result, total_steps)
    series_cache[n] = series
    
    return result, total_steps, series

# Sample direct function calls (replace n with any value you want to test):
n = int(input("Enter a number: "))

# Iterative approach
iter_result, iter_steps, iter_series = fibonacci_iter(n)
print("Iterative Fibonacci:", iter_result)
print("Steps:", iter_steps)
print("Series:", iter_series)

# Recursive approach (with warning for large values)
if n > 1000:
    print(f"\nWarning: n={n} is very large. Recursive approach may be slow or hit recursion limits.")
    print("Consider using the iterative approach for large values.")
    response = input("Continue with recursive approach? (y/n): ")
    if response.lower() != 'y':
        print("Skipping recursive calculation.")
    else:
        try:
            # Increase recursion limit for very large values
            sys.setrecursionlimit(max(10000, n * 2))
            recur_result, recur_steps, recur_series = fibonacci_recur(n)
            print("Recursive Fibonacci:", recur_result)
            print("Steps:", recur_steps)
            print("Series:", recur_series)
        except RecursionError:
            print("RecursionError: Value too large for recursive approach. Use iterative method instead.")
else:
    recur_result, recur_steps, recur_series = fibonacci_recur(n)
    print("Recursive Fibonacci:", recur_result)
    print("Steps:", recur_steps)
    print("Series:", recur_series)
