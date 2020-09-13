import numpy as np

pythonList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numpyArray = np.array(pythonList, dtype=int)

print(f"Python List     : {pythonList}")
print(f"NumpyArray      : {numpyArray}")


zerosNedir = np.zeros(10, dtype=int)
print(zerosNedir)

onesNedir = np.ones((3,5), dtype=int)
print(onesNedir)

fullNedir = np.full((3,5), 3, dtype=int)
print(fullNedir)

arangeNedir = np.arange(0, 31, 3)
print(arangeNedir)

linspaceNedir = np.linspace(0, 1, 10)
print(linspaceNedir)

randomNormalNedir = np.random.normal(10, 4, (3,4))
randomRandintNedir = np.random.randint(0, 10, (3,3))
print(randomNormalNedir)
print(randomRandintNedir)