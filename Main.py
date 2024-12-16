import numpy as np
import matplotlib.pyplot as plt

# Function to simulate marble drops
def simulate_marble_drops(total_drops):
    # Define Table boundaries as a rectangle
    table_x, table_y, table_width, table_height = -1.5, -1.5, 4.5, 3  # (x, y) at (-1.5, -1.5), size 4.5x3

    # Define Circular Tray parameters
    circle_center_x, circle_center_y, circle_radius = 0, 0, 1  # Center at (0,0), radius = 1

    # Define Rectangular Tray parameters
    rect_x, rect_y, rect_width, rect_height = 1.5, -1, 1, 2  # Bottom-left corner (1.5,-1), size 1x2

    # Generate all random drops at once
    x_vals = np.random.uniform(table_x, table_x + table_width, total_drops)
    y_vals = np.random.uniform(table_y, table_y + table_height, total_drops)

    # Vectorized calculations for circular tray
    distances = (x_vals - circle_center_x)**2 + (y_vals - circle_center_y)**2
    circle_mask = distances <= circle_radius**2

    # Vectorized calculations for rectangular tray
    rectangle_mask = (rect_x <= x_vals) & (x_vals <= rect_x + rect_width) & \
                     (rect_y <= y_vals) & (y_vals <= rect_y + rect_height)

    # Identify missed marbles (outside both trays)
    misses_mask = ~(circle_mask | rectangle_mask)

    # Count marbles in trays
    count_in_circle = np.sum(circle_mask)
    count_in_rectangle = np.sum(rectangle_mask)

    # Extract positions for visualization
    circle_hits = np.column_stack((x_vals[circle_mask], y_vals[circle_mask]))
    rectangle_hits = np.column_stack((x_vals[rectangle_mask], y_vals[rectangle_mask]))
    misses = np.column_stack((x_vals[misses_mask], y_vals[misses_mask]))

    # Compute probabilities
    prob_circle = count_in_circle / total_drops
    prob_rectangle = count_in_rectangle / total_drops

    # Estimate Pi
    estimated_pi = 2 * prob_circle  # π ≈ 2 * (Marbles in Circle / Total Drops)

    # Output results
    print("Simulation Results:")
    print(f"Total Marble Drops: {total_drops}")
    print(f"Marbles in Circular Tray: {count_in_circle} (Probability: {prob_circle:.2f})")
    print(f"Marbles in Rectangular Tray: {count_in_rectangle} (Probability: {prob_rectangle:.2f})")
    print(f"Estimated Pi: {estimated_pi:.5f}")

    # Visualization
    plt.figure(figsize=(12, 8))
    plt.xlim(table_x, table_x + table_width)
    plt.ylim(table_y, table_y + table_height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Monte Carlo Simulation")
    plt.xlabel("X-axis (Table Width)")
    plt.ylabel("Y-axis (Table Height)")

    # Draw the trays
    circle = plt.Circle((circle_center_x, circle_center_y), circle_radius, color='blue', fill=False, linewidth=2, label='Circular Tray')
    rect = plt.Rectangle((rect_x, rect_y), rect_width, rect_height, color='red', fill=False, linewidth=2, label='Rectangular Tray')
    plt.gca().add_patch(circle)
    plt.gca().add_patch(rect)

    # Plot marbles
    if len(circle_hits) > 0:
        plt.scatter(circle_hits[:, 0], circle_hits[:, 1], color='blue', s=10, label='Marbles in Circular Tray')
    if len(rectangle_hits) > 0:
        plt.scatter(rectangle_hits[:, 0], rectangle_hits[:, 1], color='red', s=10, label='Marbles in Rectangular Tray')
    if len(misses) > 0:
        plt.scatter(misses[:, 0], misses[:, 1], color='gray', s=10, label='Missed Marbles')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    total_drops = 10000 # Total number of marble drops
    simulate_marble_drops(total_drops)
