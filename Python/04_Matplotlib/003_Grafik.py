import matplotlib.pyplot as plt
import numpy as np

figur = plt.figure()
data = np.random.randn(50).cumsum()
ozellik = {
    "title": "Grafik Tesk",
    "xlabel": "Adımlar",
    "ylabel": "Sayılar"
}


veriBir = [1, 2, 3, 4, 5]
veriIki = [10, 11, 12, 13, 14]

bir = figur.add_subplot(2, 2, 1)
bir.plot(veriBir, veriIki, "k-")

iki = figur.add_subplot(2, 2, 2)
iki.plot(data, "b^-.")

uc = figur.add_subplot(2, 2, 3)
uc.plot(data, "ro--")
uc.set_xticks([0, 15, 30, 45])
uc.set_xticklabels(['bir', 'iki', 'uc', 'dort'], rotation=30, fontsize='small')

dort = figur.add_subplot(2, 2, 4)
dort.plot(veriBir, veriIki, linestyle="dashdot", color="green", label="Veri Başlığı")
dort.set(**ozellik)

if __name__ == "__main__":
    plt.legend()
    plt.show()