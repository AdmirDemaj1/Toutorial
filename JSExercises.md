Given a set of coin values coins={c1,c2, ..., ck} and a target sum of money m, whats the minimum number of coins that form the sum m? Consider the cons to be in euros.

Input:
coins : {1, 4 , 5}
targetSum: 13

Answer should be 4,4,4,1.

```JavaScript
function minCoins(coins, targetSum) {
  // Initialize an array to store minimum number of coins needed for each target sum
  const dp = new Array(targetSum + 1).fill(Infinity);
  dp[0] = 0; // Zero coins needed to make a sum of zero

  // Iterate through each coin and update the dp array
  for (const coin of coins) {
    for (let i = coin; i <= targetSum; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  console.log(dp);

  // Reconstruct the solution by backtracking through the dp array
  const result = [];
  let remaining = targetSum;

  while (remaining > 0) {
    for (const coin of coins) {
      console.log("coin", coin);
      console.log(
        "dp[remaining - coin] + 1 === dp[remaining]",
        dp[remaining - coin] + 1,
      );
      if (remaining - coin >= 0 && dp[remaining - coin] + 1 === dp[remaining]) {
        result.push(coin);

        remaining -= coin;

        break;
      }
    }
  }

  return result;
}

const coins = [1, 4, 5];
const targetSum = 13;

const minCoinsResult = minCoins(coins, targetSum);
console.log(minCoinsResult);
```
