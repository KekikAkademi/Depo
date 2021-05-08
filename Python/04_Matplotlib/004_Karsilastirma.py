import matplotlib.pyplot as plt
import numpy as np

figur = plt.figure()

ax = figur.add_subplot(1, 1, 1)

veriBir = np.random.randn(10).cumsum()
veriIki = np.random.randn(10).cumsum()
veriUc = np.random.randn(10).cumsum()

ax.plot(veriBir, "k-.", label="Bir")
ax.plot(veriIki, "bo-", label="İki")
ax.plot(veriUc, "r^-", label="Üç")

if __name__ == "__main__":
    plt.title("Grafik Başlığı")
    plt.legend()
    plt.show()