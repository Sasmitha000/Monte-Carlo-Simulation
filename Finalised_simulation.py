import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from openpyxl.drawing.image import Image
import os

# Initialize your constants here
actual_pi = np.pi
runs = [100, 1000, 10000, 100000, 1000000]  # Different point samples to test

# Define the table boundaries (as a rectangle)
table_x, table_y, table_z = -1.5, -1.5, 0  # Bottom-left corner of the table (x, y), z is the bottom height
table_length, table_width, table_height = 4.5, 3, 1  # Length, width, height of the table

# Cuboid tray properties (length, width, height)
cuboid_x, cuboid_y, cuboid_z = 1.5, -1, 0  # Bottom-left corner (x, y), z is the bottom height
cuboid_length, cuboid_width, cuboid_height = 2, 1, 1  # Length, width, height of the cuboid

# Cylinder tray properties (radius and height)
cylinder_x, cylinder_y, cylinder_z = 0, 0, 0  # Center of the cylinder at (x, y) with base at z=0
cylinder_radius = 1  # Radius of the circular base
cylinder_height = 1  # Height of the cylinder

# Create an empty list to store all the PI values for plotting
pi_values = []
results = []

# Create an Excel writer to save all data to one sheet
with pd.ExcelWriter('monte_carlo_pi_simulation.xlsx', engine='openpyxl') as writer:
    # Create a new sheet for all the data
    workbook = writer.book
    sheet = workbook.create_sheet('Monte Carlo Results')

    current_row = 1  # Row to start inserting data

    for num_points in runs:
        pi_run_values = []  # List to store PI values for multiple trials
        run_results = []  # Store the results of each run for each sample size

        # Add a header for the current sample size
        sheet.cell(row=current_row, column=1, value=f"Results for {num_points} Points")
        current_row += 1

        # Run each experiment 10 times
        for _ in range(10):
            # Initialize counters for each run
            inside_cylinder = 0
            inside_cuboid = 0
            inside_table = 0

            # Generate random points within the table boundaries using numpy
            x_points = np.random.uniform(table_x, table_x + table_length, num_points)
            y_points = np.random.uniform(table_y, table_y + table_width, num_points)
            z_points = np.random.uniform(0, 1, num_points)  # Generate random z-coordinates for 3D

            # Loop through each point and check if it falls inside the table, cylinder, or cuboid
            for i in range(num_points):
                x = x_points[i]
                y = y_points[i]
                z = z_points[i]

                # Check if the point is inside the table (in 3D)
                if table_x <= x <= table_x + table_length and table_y <= y <= table_y + table_width and table_z <= z <= table_z + table_height:
                    inside_table += 1

                    # Check if the point is inside the cylinder (in 3D)
                    if (x - cylinder_x)**2 + (y - cylinder_y)**2 <= cylinder_radius**2 and cylinder_z <= z <= cylinder_z + cylinder_height:
                        inside_cylinder += 1

                    # Check if the point is inside the cuboid (in 3D)
                    if cuboid_x <= x <= cuboid_x + cuboid_length and cuboid_y <= y <= cuboid_y + cuboid_width and cuboid_z <= z <= cuboid_z + cuboid_height:
                        inside_cuboid += 1

            # Calculate probabilities for the three trays
            table_probability = inside_table / num_points
            cylinder_probability = inside_cylinder / num_points
            cuboid_probability = inside_cuboid / num_points

            # Estimate areas based on probabilities
            cylinder_area_estimate = cylinder_probability * (table_length * table_width * table_height)
            cuboid_area_estimate = cuboid_probability * (table_length * table_width * table_height)

            # Estimate PI from the cylinder area (same logic as before)
            pi_estimate = cylinder_area_estimate / (cylinder_radius**2)
            pi_run_values.append(pi_estimate)  # Store this run's PI value

            # Calculate difference from actual PI
            pi_difference = abs(pi_estimate - actual_pi)
            run_results.append({
                'Run': len(run_results) + 1,
                'PI Value': pi_estimate,
                'Difference from PI': pi_difference
            })

        # Calculate mean and mode for the 10 runs
        mean_pi = np.mean(pi_run_values)
        mode_result = stats.mode(pi_run_values)

        # Check and extract the mode value safely
        if isinstance(mode_result.mode, np.ndarray):
            pi_mode = mode_result.mode[0]  # If it's an array, access the first element
        else:
            pi_mode = mode_result.mode  # If it's scalar, just assign it

        # Append mean, mode and difference from actual PI for this sample size
        results.append({
            'Points': num_points,
            'Mean PI': mean_pi,
            'Mode PI': pi_mode,
            'Difference from Actual PI': abs(mean_pi - actual_pi)
        })

        # Store the PI values for plotting later
        pi_values.append(mean_pi)

        # Create a DataFrame for the results of this sample size
        df_run_results = pd.DataFrame(run_results)

        # Write the run results to the sheet
        df_run_results.to_excel(writer, sheet_name='Monte Carlo Results', startrow=current_row, index=False)

        # Update the row to the next available row after writing the data
        current_row += len(df_run_results) + 2  # 2 extra rows for spacing

    # Save the summary results in the same sheet
    df_summary = pd.DataFrame(results)
    df_summary.to_excel(writer, sheet_name='Monte Carlo Results', startrow=current_row, index=False)

    # Plot the PI values against N and save the plot
    plt.plot(runs, pi_values, marker='o', label='Estimated PI')
    plt.axhline(y=actual_pi, color='r', linestyle='--', label='Actual PI')
    plt.xlabel('Number of Points (N)')
    plt.ylabel('Estimated PI')
    plt.title('Estimated PI vs. Number of Points')
    plt.legend()
    plt.savefig('monte_carlo_pi_plot.png')
    plt.close()

    # Write the plot to the Excel file
    img = Image('monte_carlo_pi_plot.png')
    sheet.add_image(img, f'A{current_row + 9}')  # Position the image after the tables

# Print the results summary
print("Monte Carlo Simulation Results Summary:")
print(df_summary)

# Automatically open the Excel file

excel_file_path = os.path.abspath('monte_carlo_pi_simulation.xlsx')

if os.name == 'nt':  # For Windows
    os.startfile(excel_file_path)
elif os.name == 'posix':  # For macOS or Linux
    os.system(f'open "{excel_file_path}"')
else:
    print("Cannot open the Excel file automatically on this operating system.")
