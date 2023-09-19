import numpy as np
import matplotlib.pyplot as plt


# Define the function representing the curve
def curve_function(x):
    return (x + 1) ** 2 - 1


# Compute the derivative of the curve function
def derivative(x):
    return 2 * (x + 1)


# Function to create a tangent line at a given point
def tangent_line(x_point):
    # Calculate the corresponding y value on the curve
    y_point = curve_function(x_point)

    # Calculate the slope of the tangent line (derivative at the point)
    slope = derivative(x_point)

    # Create the equation of the tangent line
    def line_equation(x):
        return slope * (x - x_point) + y_point

    return line_equation


# Generate x values
x = np.linspace(-10, 10, 400)
y = curve_function(x)

# Choose a point to find the tangent line
x_point = 2
y_point = curve_function(x_point)

# Create the tangent line function for the chosen point
tangent = tangent_line(x_point)

# Plot the curve and the tangent line
plt.figure(figsize=(8, 6))

plt.plot(x, y, label="y = (x + 1)^2 - 1", color='yellow')
plt.plot(x, tangent(x), label=f"Tangent at x = {x_point}", linestyle='--', color='red')
plt.scatter(x_point, y_point, color='red', label=f'Point ({x_point}, {y_point})', zorder=5)
plt.xlabel('Cirrus', color='white')
plt.ylabel('Astrid', color='white')
plt.title('Graph of y = (x + 1)^2 - 1 with Tangent Line', color='white')
plt.grid(True)
plt.legend()
plt.show()
