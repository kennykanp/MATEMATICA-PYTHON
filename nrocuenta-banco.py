# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# from array import *
#https://docs.python.org/3/library/array.html

import numpy as npn
#https://numpy.org/doc/stable/user/quickstart.html

# TODO: Do this
# filtrar  ==========================> Listo!!!
# luego listar todo =================> Listo (el mas facil)
# Agregar agregar array =============> Listo!!!
# actualizar ========================>

# b = npn.array([[ 0,  1],
#                [10, 11],
#                [20, 21],
#                [30, 31],
#                [40, 41]])

b = [];

def fn_abriCuenta(pBanco, pCuenta):
    if len(pBanco) > 0 :
        for i in pBanco:
            if i[0] == pCuenta :
                print('ya existe pe')
                return pBanco

        b = npn.append(pBanco, [[pCuenta, len(pBanco)+1]], 0)
        print(b)
        return b
    else:
        print('mi primera vez fue ..... uwu')
        b = npn.array([[pCuenta, 1]])
        print(b)
        return b

v = fn_abriCuenta(b, 70)
v = fn_abriCuenta(v, 80)
v = fn_abriCuenta(v, 90)
v = fn_abriCuenta(v, 90)
v = fn_abriCuenta(v, 100)
v = fn_abriCuenta(v, 150)
v = fn_abriCuenta(v, 150)
v = fn_abriCuenta(v, 200)


print('Copyright •2021 (yo bb)')