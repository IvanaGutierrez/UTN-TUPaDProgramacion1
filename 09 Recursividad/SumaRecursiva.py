# Suma recursiva
"""Pasando una lista de numeros, 
obtener la suma total de los mismos en forma recursiva"""


def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0]+sum_list(lst[1:])
