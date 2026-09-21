def knapsack_bottom_up(values, weights, W):

    n = len(values)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(W + 1):

            if weights[i - 1] <= w:

                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                if include > exclude:
                    dp[i][w] = include
                else:
                    dp[i][w] = exclude

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


def knapsack_top_down(values, weights, W):

    n = len(values)

    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def solve(i, w):

        if i == 0 or w == 0:
            return 0

        if memo[i][w] != -1:
            return memo[i][w]

        if weights[i - 1] > w:
            memo[i][w] = solve(i - 1, w)

        else:
            include = values[i - 1] + solve(
                i - 1, w - weights[i - 1]
            )

            exclude = solve(i - 1, w)

            if include > exclude:
                memo[i][w] = include
            else:
                memo[i][w] = exclude

        return memo[i][w]

    return solve(n, W)


print("0/1 KNAPSACK PROBLEM")
print("--------------------")

n = int(input("Enter number of items: "))

values = []
weights = []

print("\nEnter values/profits of items:")
for i in range(n):
    value = int(input("Value of item " + str(i + 1) + ": "))
    values.append(value)

print("\nEnter weights of items:")
for i in range(n):
    weight = int(input("Weight of item " + str(i + 1) + ": "))
    weights.append(weight)

W = int(input("\nEnter maximum capacity of knapsack: "))

bottom_up_result = knapsack_bottom_up(values, weights, W)

top_down_result = knapsack_top_down(values, weights, W)

print("\n--------------------")
print("RESULT")
print("--------------------")

print("Maximum value using Bottom-Up:", bottom_up_result)
print("Maximum value using Top-Down:", top_down_result)