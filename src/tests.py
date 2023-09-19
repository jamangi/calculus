import numpy as np
import matplotlib.pyplot as plt

# Generate x values ♡
x = np.linspace(-10, 10, 20)

# Calculate y values using y = 2x ♡
y = (x + 1)**2 -1

# Set the style ♡
plt.style.use('dark_background')  # Use a dark background style ♡

# Create the plot ♡
plt.figure(figsize=(8,6))
plt.plot(x, y, label="y = (x + 1)^2 - 1", color='yellow')

# Add labels and title ♡
plt.xlabel('Cirrus', color='white')
plt.ylabel('Astrid', color='white')
plt.title('Graph of y = (x + 1)^2 - 1', color='white')

# Display the plot ♡
plt.grid(True)
plt.show()
