import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签, windows
plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 用来正常显示中文标签, mac


def degree2rad(degree):
    return degree * np.pi / 180


def rad2degree(rad):
    return rad * 180 / np.pi


def BLH2xyz(L, B, H, rad=True):
    if not rad:
        L = degree2rad(L)
        B = degree2rad(B)
    a = 6378137.0000
    b = 6356752.3141
    e2 = 1 - (b / a)**2
    N = a/np.sqrt(1-e2*np.sin(B)**2)
    x = (N + H) * np.cos(B) * np.cos(L)
    y = (N + H) * np.cos(B) * np.sin(L)
    z = (N * (1 - e2) + H) * np.sin(B)
    return x, y, z


def dB2distance(dB, rad=True):
    if not rad:
        dB = degree2rad(dB)
    a = 6378137.0000
    b = 6356752.3141
    r = (a + b) / 2  # 近似
    return r*dB


if __name__ == '__main__':
    a = 6378137.0000
    b = 6356752.3141
    e2 = 1 - (b / a)**2
    L, H = degree2rad(116), 235
    B =  degree2rad(np.linspace(0, 80, 160))
    x, y, z = BLH2xyz(L, B, H, rad=True)
    p = np.sqrt(x**2+y**2)
    N = a/np.sqrt(1-e2*np.sin(B)**2)
    theta = np.arctan(z*a/(p*b))
    realB = np.arctan(z*(N+H)/((N*(1-e2)+H)*p))
    fakeB = np.arctan((z+e2*b*np.sin(theta)**3)/(p-e2*a*np.cos(theta)**3))
    dis = dB2distance(fakeB-realB, rad=True)
    plt.plot(rad2degree(B),dis)
    plt.show()
