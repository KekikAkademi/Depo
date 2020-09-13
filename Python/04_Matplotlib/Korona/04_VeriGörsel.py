import pandas as pd

pandaVeri = pd.read_csv("novel-corona-virus-2019-dataset/covid_19_data.csv").rename(columns={
    "ObservationDate": "Gözlem Tarihi",
    "Province/State": "İl / Eyalet",
    "Country/Region": "Ülke / Bölge",
    "Last Update": "Son Güncelleme",
    "Confirmed": "Vaka",
    "Deaths": "Ölü",
    "Recovered": "Taburcu"
    })

pandaVeri = pandaVeri.drop(columns="SNo").drop(columns="İl / Eyalet")

turkiye = pandaVeri[pandaVeri["Ülke / Bölge"] == "Turkey"]
vaka = turkiye['Vaka']
taburcu = turkiye['Taburcu']
olu = turkiye['Ölü']

import matplotlib.pyplot as plt

# plt.plot(vaka, label="Vaka")
# plt.plot(taburcu, label="Taburcu")
# plt.xlabel("Vaka Sayısı")
# plt.ylabel("Taburcu Sayısı")
# plt.legend()
# plt.title("Türkiye Covid-19")
# plt.show()

####

# pandaVeri.plot(subplots=True)

# plt.subplot(2, 1, 1)
# plt.title("Türkiye Covid-19")
# plt.plot(vaka, taburcu, "g-", label="Vaka/Taburcu")
# plt.ylabel("Taburcu")
# plt.legend()


# plt.subplot(2, 1, 2)
# plt.plot(vaka, olu, "r:", label="Vaka/Ölü")
# plt.xlabel("Vaka")
# plt.ylabel("Ölü")
# plt.legend()

# plt.show()

####


plt.plot(taburcu, "g:", label="Taburcu")
plt.plot(olu, "r-", label="Ölü")

plt.legend()
plt.show()