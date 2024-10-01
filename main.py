from sum_file import affichesum
from moyen_file.py import calcul_moyenne


nombres = [1.0, 2.0, 3.0]
print("Data list :")
print(nombres)

print("---------------")
somme, nombre_elements = affichesum(nombres)
print("Somme :", somme)
print("Nombre d'éléments :", nombre_elements)

print("---------------")
moyenne, min_val, max_val = calcul_moyenne(nombres)
print("Moyenne :", moyenne)
print("Min :", min_val)
print("Max :", max_val)