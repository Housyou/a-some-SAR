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


def accurate(x, y, z, rad=True):
    a = 6378137.0000
    b = 6356752.3141
    e2 = 1 - (b / a)**2
    p = np.sqrt(x**2+y**2)
    L = np.arctan2(y, x)

    def ite(z, p):
        def cal_N(B): return a/np.sqrt(1-e2*np.sin(B)**2)
        def cal_H(N, B): return p/np.cos(B)-N
        def cal_B(N, H): return np.arctan(z/((1 - e2*N/(N+H))*p))
        B = cal_B(1, 0)
        N = cal_N(B)
        H0, H = 1e9, cal_H(N, B)
        while np.abs(H - H0) > 0.1:
            B = cal_B(N, H)
            N = cal_N(B)
            H0, H = H, cal_H(N, B)
        return H, B

    H, B = np.vectorize(ite)(z, p)
    if rad:
        return L, B * 1, H * 1
    else:
        return rad2degree(L), rad2degree(B), H * 1


def rough(x, y, z, rad=True):
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


def dB2distance(dB, rad=True):
    if not rad:
        dB = degree2rad(dB)
    a = 6378137.0000
    b = 6356752.3141
    r = (a + b) / 2  # 近似
    return r*dB


if __name__ == '__main__':
    L = 116
    Bmin, Bmax, Bnum = 0, 80, 160
    Hmin, Hmax, Hnum = -500, 8000, 500
    B = np.linspace(Bmin, Bmax, Bnum + 1)
    H = np.linspace(Hmin, Hmax, Hnum + 1)
    B, H = np.meshgrid(B, H)
    x, y, z = BLH2xyz(L, B.ravel(), H.ravel(), rad=False)
    la, ba, ha = accurate(x, y, z, rad=False)
    lr, br, hr = rough(x, y, z, rad=False)

    def plot(img, title):
        ax = plt.gca()
        ai = ax.imshow(img, aspect='auto', cmap='rainbow')
        ax.set_xlim(0, Bnum)
        ax.set_xticks([0, Bnum/2, Bnum])
        ax.set_xticklabels([Bmin, np.mean([Bmin, Bmax]), Bmax])
        ax.set_xlabel(r'$B (\degree)$')
        ax.set_ylim(0, Hnum)
        ax.set_yticks([0, Hnum/2, Hnum])
        ax.set_yticklabels([Hmin, (Hmin+Hmax)/2, Hmax])
        ax.set_ylabel(r'$H (m)$')
        plt.colorbar(ai, ax=ax).set_label('m')
        plt.title(title)

    def show_H():
        dH = (ha - hr).reshape((Hnum + 1, -1))
        plot(dH, r'$\Delta H (m)$高程误差')
        plt.show()

    def show_B():
        dB = dB2distance(br-ba, rad=False).reshape((Hnum + 1, -1))
        plot(dB, r'南北距离误差 (m)')
        plt.show()

    show_H()
    # show_B()