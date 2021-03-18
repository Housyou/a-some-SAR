import numpy as np


def rad2degree(rad):
    return rad * 180 / np.pi


def xyz2BLH(x, y, z, rad=True):
    a = 6378137.0000
    b = 6356752.3141
    e2 = 1 - (b / a)**2
    p = np.sqrt(x**2+y**2)
    theta = np.arctan(z * a/(p * b))
    L = np.arctan2(y, x)
    B = np.arctan((z + e2*b*np.sin(theta)**3)/(p - e2*a*np.cos(theta)**3))
    N = a/np.sqrt(1-e2*np.sin(B)**2)
    H = p / np.cos(B) - N
    if rad:
        return L, B, H
    else:
        return rad2degree(L), rad2degree(B), H


# L, B, H = 116, 40, 235
# print(BLH2xyz(L, B, H, rad=False))
x, y, z = -2144900.7573362007, 4397698.262572753, 4078136.627140711
print(xyz2BLH(x, y, z, rad=False))
# (116.0, 39.99947761910426, 186.3290731832385)
