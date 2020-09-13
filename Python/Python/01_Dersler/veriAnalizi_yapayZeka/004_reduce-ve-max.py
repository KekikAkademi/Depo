"""

"""

from functools import reduce
reduceTest = reduce(lambda sayi1, sayi2 : sayi1*sayi2, [1, 2, 3, 4,5])
print(reduceTest)
"""
1*2  = 2
2*3  = 6
6*   = 24
24*5 = 120
"""

maxTest = max([1, 2, 3, 4, 5])              # Rakamsal en Büyük değer
print(maxTest)
maxTest2 = max(['Ali', 'Mehmet', 'Ayşe'])   # Alfabetik en büyük değer
print(maxTest2)
#maxTest3 = max([7, 5, 'Ali','Mehmet','Ayşe'])       # TypeError: '>' not supported between instances of 'str' and 'int'