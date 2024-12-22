import random

def simulate_family():
    # Generate a family of 3 children, 0 for boy, 1 for girl
    family = [random.choice([0, 1]) for _ in range(3)]
    return family

def check_all_girls(family):
    return all(child == 1 for child in family)

def check_at_least_one_girl(family):
    return any(child == 1 for child in family)

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
print(f"\nProbability: {probability:.4f}/n")
