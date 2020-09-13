import matplotlib.pyplot as plt
import numpy as np

veri = np.arange(0., 5., 0.2)

plt.plot(veri, veri, "r--", veri, veri**2, "bs", veri, veri**3, "g^")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.title("Grafik Başlığı")

plt.savefig("002_pngCikti.png")
plt.savefig("002_pdfCikti.pdf", dpi=500, bbox_inches="tight")

if __name__ == "__main__":
    plt.show()