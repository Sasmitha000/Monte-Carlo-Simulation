import numpy as np

# Dynamic programming approach to count all ways to get a sum of 30 with 10 dice
def count_all_ways(target_sum, num_dice):
    # dp[i][j] will store the number of ways to get sum j with i dice
    dp = np.zeros((num_dice + 1, target_sum + 1), dtype=int)
    
    # There is one way to get a sum of 0 with 0 dice (the empty set)
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, num_dice + 1):
        for j in range(1, target_sum + 1):
            for face in range(1, 7):  # Each die can show values from 1 to 6
                if j - face >= 0:
                    dp[i][j] += dp[i - 1][j - face]
    
    # Extract all possible combinations that sum to target_sum
    def find_combinations(i, j, current_combination):
        if i == 0 and j == 0:
            all_combinations.append(list(current_combination))
            return
        if i == 0 or j == 0:
            return
        
        for face in range(1, 7):
            if j - face >= 0 and dp[i - 1][j - face] > 0:
                current_combination.append(face)
                find_combinations(i - 1, j - face, current_combination)
                current_combination.pop()
    
    all_combinations = []
    find_combinations(num_dice, target_sum, [])
    
    return dp[num_dice][target_sum], all_combinations

# Simulation function
def simulate_dice_rolls(num_simulations, num_dice, target_sum):
    count = 0
    
    for _ in range(num_simulations):
        rolls = np.random.randint(1, 7, num_dice)
        if rolls.sum() == target_sum:
            count += 1
    
    probability = count / num_simulations
    return probability

# Parameters
num_simulations = 500
num_dice = 10
target_sum = 30

# Step 1: Calculate exact number of ways and display combinations
total_ways, all_combinations = count_all_ways(target_sum, num_dice)
print(f"Total ways to make {target_sum} with {num_dice} dice: {total_ways}")
print(f"Displaying all possible combinations that sum to {target_sum}:")
for combination in all_combinations[:10]:  # Display first 10 combinations
    print(combination)

# Step 2: Run simulation
probability = simulate_dice_rolls(num_simulations, num_dice, target_sum)
print(f"Estimated Probability of making {target_sum} with {num_dice} dice: {probability:.4f}")
