import numpy as np

def simulate_family():
    # Generate a family of 3 children, 0 for boy, 1 for girl
    return np.random.choice([0, 1], size=3)

def check_all_girls(family):
    return np.all(family == 1)

def check_at_least_one_girl(family):
    return np.any(family == 1)

# Simulation: Run 1000 times
num_trials = 1000
all_girls_given_one_girl = 0
at_least_one_girl_count = 0

for _ in range(num_trials):
    family = simulate_family()
    
    if check_at_least_one_girl(family):
        at_least_one_girl_count += 1
        if check_all_girls(family):
            all_girls_given_one_girl += 1

# Calculate the probability from the simulation
probability = all_girls_given_one_girl / at_least_one_girl_count
print(f"Simulated Probability: {probability:.4f}")
