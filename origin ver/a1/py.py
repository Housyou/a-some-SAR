import matplotlib.pyplot as plt
import numpy as np

start, end, num = -1, 1, 1000
var = np.linspace(start, end, num + 1)  # 变量区间[-1,1]，在这之中取1001个数
x, y = np.meshgrid(var, var)
# x, y的shape都是(1001,1001)，表示这1001x1001个点的二维坐标


def plot(index, img, title, color_ticks, color_ticklabels):
    ax = plt.subplot(1, 2, index)
    ax.spines['right'].set_color('none')  # 调整坐标轴的位置
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', num / 2))
    ax.spines['left'].set_position(('data', num / 2))
    blank = num * 0.1
    ax.set_xlim(-blank, num + blank)
    ax.set_ylim(-blank, num + blank)  # 若不调整，y轴方向朝下
    ax.set_xticks([0, num])  # 因为有1001个点，所以取值范围是[0,1000]
    ax.set_xticklabels([start, end])  # 把取值还原回[-1,1]
    ax.set_yticks([0, num])
    ax.set_yticklabels([start, end])
    ax.set_title(title)
    ai = ax.imshow(img, cmap='rainbow')
    colorbar = plt.colorbar(ai, ax=ax)
    colorbar.set_ticks(color_ticks)
    colorbar.set_ticklabels(color_ticklabels)


z = np.arctan(y / x) / np.pi
plot(1, z, 'arctan(y/x)', [-0.49, -0.25, 0, 0.25, 0.49],
     [r'$-0.49\pi$', r'$-\pi/4$', '0', r'$\pi/4$', r'0.49$\pi$'])

z = np.arctan2(y, x) / np.pi
plot(2, z, 'arctan2(y,x)', [-0.99, -0.5, 0, 0.5, 1],
     [r'$-0.99\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])

plt.show()
