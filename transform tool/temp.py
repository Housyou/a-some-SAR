import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签, windows
plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 用来正常显示中文标签, mac


def degree2rad(degree):
    return degree * np.pi / 180


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


def cal_times(x, y, z, limit):
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
        count = 0
        while np.abs(H - H0) > limit:
            count += 1
            B = cal_B(N, H)
            N = cal_N(B)
            H0, H = H, cal_H(N, B)
        return count
    times = np.vectorize(ite)(z, p)
    return times


if __name__ == '__main__':
    L = 116
    Bmin, Bmax, Bnum = 0, 80, 120
    Hmin, Hmax, Hnum = -500, 8000, 425
    B = np.linspace(Bmin, Bmax, Bnum + 1)
    H = np.linspace(Hmin, Hmax, Hnum + 1)
    B, H = np.meshgrid(B, H)
    x, y, z = BLH2xyz(L, B.ravel(), H.ravel(), rad=False)

    def plot(index, limit):
        times = cal_times(x, y, z, limit)
        img = times.reshape((Hnum+1, Bnum+1))
        ax = plt.subplot(2, 2, index)
        ai = ax.imshow(img, aspect='auto', cmap='gray')
        ax.set_xlim(0, Bnum)
        ax.set_xticks([0, Bnum/2, Bnum])
        ax.set_xticklabels([Bmin, np.mean([Bmin, Bmax]), Bmax])
        ax.set_xlabel(r'$B (\degree)$')
        ax.set_ylim(0, Hnum)
        ax.set_yticks([0, Hnum/2, Hnum])
        ax.set_yticklabels([Hmin, (Hmin+Hmax)/2, Hmax])
        ax.set_ylabel(r'$H (m)$')
        ax.set_title('精度 %.1e m' % limit)
        plt.colorbar(ai, ax=ax).set_label('迭代次数')
    plot(1,1)
    plot(2,0.1)
    plot(3,1e-3)
    plot(4,1e-6)
    plt.show()
