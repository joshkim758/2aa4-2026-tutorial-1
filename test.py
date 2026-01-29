import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 20, 10)
plt.plot(x, 2*x)
plt.title("Test Plot")
plt.savefig("test_plot.png")
print("Test Plot saved successfully!")