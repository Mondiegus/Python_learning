import numpy as np
import pandas as pd


class okon(Exception):
    pass


deg = input('Podaj kat: ')
deg = float(deg)

rad = np.deg2rad(deg)

try:
    if 180 == deg or 0 == deg:
        raise okon("LAMA")
    sin = np.sin(rad)
    cos = np.cos(rad)
    tan = np.tan(rad)
    ctg = 1/np.tan(rad)
    print(f'Sinus: {sin}')
    print(f'Sinus: {cos}')
    print(f'Sinus: {tan}')
    print(f'Sinus: {ctg90}')
except okon:
    print("LAMA")
