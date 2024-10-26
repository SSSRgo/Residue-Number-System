
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 7  # Number of roots of unity
x = 1  # Fixed x value for calculation
delta_x_range = np.arange(-10, 10.1, 0.1)  # Range of delta_x values

# Define theta values for the N roots of unity
theta = 2 * np.pi * np.arange(N) / N

# Compute z(x) and z(x + delta_x) for each delta_x in the specified range
similarities = []
for delta_x in delta_x_range:
    z_x = np.exp(1j * theta * x)
    z_x_delta = np.exp(1j * theta * (x + delta_x))
    similarity = np.real(np.dot(z_x, np.conj(z_x_delta))) / N
    similarities.append(similarity)

# Plotting the similarity kernel
plt.figure(figsize=(10, 5))
plt.plot(delta_x_range, similarities)
plt.title("Similarity Kernel for N=7")
plt.xlabel(r"$\Delta x$")
plt.ylabel(r"$z(x) \cdot z(x + \Delta x)$")
plt.grid(True)
plt.show()
