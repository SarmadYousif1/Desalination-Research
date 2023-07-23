import matplotlib.pyplot as plt
import numpy as np

# Create the data
salinity = 50
oxygen = 20
pollutants = 30

# Calculate the total to get percentages
total = salinity + oxygen + pollutants
salinity_percentage = salinity / total * 100
oxygen_percentage = oxygen / total * 100
pollutants_percentage = pollutants / total * 100

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')  # To make the plot circular

# Create the slices of the circle
slices, _ = ax.pie([salinity_percentage, oxygen_percentage, pollutants_percentage], colors=["red", "blue", "green"], startangle=90)

# Add labels to the slices with percentage values
labels = [f"Increased salinity\n{salinity_percentage:.1f}%",
          f"Decreased oxygen levels\n{oxygen_percentage:.1f}%",
          f"Introduction of pollutants\n{pollutants_percentage:.1f}%"]

for label, slice in zip(labels, slices):
    x, y = slice.center
    theta = slice.theta1 + 0.4 * (slice.theta2 - slice.theta1)
    x_text = x + 1.7 * slice.r * np.cos(np.radians(theta))  # Move the text horizontally
    y_text = y + 1.4 * slice.r * np.sin(np.radians(theta))  # Move the text vertically
    ax.text(x_text, y_text, label, ha='center', va='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white"))

# Calculate the mid_x and mid_y values based on the range of data coordinates
mid_x = (np.max([s.center[0] for s in slices]) + np.min([s.center[0] for s in slices])) / 2
mid_y = np.min([s.center[1] for s in slices])

# Combine the percentage values of all three slices and add some additional text
additional_text = "and more"  # Add your desired additional text here
combined_text = f"Total: {total:.1f}% {additional_text}"

# Add the combined text label to the specified position and align it to the bottom
ax.text(mid_x, mid_y, combined_text, ha='center', va='bottom', fontsize=12)

# Add a title and show the plot
plt.title("Percentage of environmental impacts of brine discharge from desalination plants")
plt.legend(slices, ["Increased salinity", "Decreased oxygen levels", "Introduction of pollutants"], loc="upper right")
plt.show()
