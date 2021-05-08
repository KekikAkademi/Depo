import matplotlib.pyplot as plt
import numpy as np

veri = np.arange(10)

plt.plot(veri, color="Green", label="Veri Başlığı")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.title("Grafik Başlığı")

if __name__ == "__main__":
    plt.legend()
    plt.show()