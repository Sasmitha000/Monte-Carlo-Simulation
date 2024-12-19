
# Monte Carlo PI Estimation

This project simulates the estimation of Pi using the Monte Carlo method, where random points are generated inside a rectangular area, and the ratio of points falling within a circle or a cuboid is used to estimate Pi.

## Installation

Before running the simulation, ensure you have the following libraries installed:

1. `numpy` - For generating random points and performing mathematical operations.
2. `pandas` - For handling data and storing results.
3. `matplotlib` - For plotting the estimated Pi values against the number of points.
4. `scipy` - For calculating statistical results (like mode).
5. `openpyxl` - For writing results to an Excel file and embedding an image in the Excel sheet.

### To install the required libraries, run:

```bash
pip install numpy pandas matplotlib scipy openpyxl
```

## Usage

To run the simulation, simply execute the Python script.

1. The program generates random points inside a cuboid and a circular tray within that cuboid.
2. It performs multiple trials to estimate the value of Pi based on the ratio of points falling inside the circle.
3. The results for each run are saved in an Excel sheet.
4. A plot is generated showing the estimated Pi values against the number of points.
5. The results are saved to an Excel file, and the plot is embedded within the same file.

### Example:

```bash
python monte_carlo_pi_simulation.py
```

## Logic Used to Estimate Pi

The estimation of Pi is based on the following Monte Carlo method:

1. **Cuboid Tray**: The cuboid tray is defined with specified dimensions. Points are randomly generated within this cuboid.
2. **Cylinder Tray**: The circle is modeled as a cylinder whose base lies inside the cuboid.
3. **Random Point Generation**: For each point, the program checks if it lies inside the cylinder (circular tray). If it does, the point contributes to the estimated area of the circle.
4. **Pi Estimation**: The ratio of points inside the circle to total points in the cuboid is used to estimate Pi.

The formula used for estimating Pi is:

```
Pi ≈ cylinder_area_estimate / (cylinder_radius**2)
```

This process is repeated for multiple runs and different sample sizes. The mean and mode of Pi values across the runs are calculated, and the results are stored in an Excel sheet.

## Results

The results include:

- Pi estimates for each run
- The difference between the estimated Pi and the actual Pi value
- The mean and mode Pi values for each sample size



