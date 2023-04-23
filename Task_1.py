def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

array1 = input("Введите массив 1 через пробел: ").split(" ")
array2 = input("Введите массив 2 через пробел: ").split(" ")
intersect = intersection(array1, array2)
intersect.sort()
print(intersect)