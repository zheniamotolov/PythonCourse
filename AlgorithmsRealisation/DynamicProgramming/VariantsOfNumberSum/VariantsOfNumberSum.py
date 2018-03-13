# n = 5
# DP = [0] * 5
# DP[0] = DP[1] = DP[2] = 1
# DP[3] = 2
# for i in range(0, n):
#     DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4]
# print(DP)

# Program to find the number of ways, n can be
# written as sum of two or more positive integers.

# Returns number of ways to write n as sum of
# two or more positive integers
def CountWays(n):
    # table[i] will be storing the number of
    # solutions for value i. We need n+1 rows
    # as the table is consturcted in bottom up
    # manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0] * (n + 1)

    # Base case (If given value is 0)
    # Only 1 way to get 0 (select no integer)
    table[0] = 1

    # Pick all integer one by one and update the
    # table[] values after the index greater
    # than or equal to n
    for i in range(1, n):

        for j in range(i, n + 1):
            table[j] += table[j - i]

    return table[n]


# driver program
