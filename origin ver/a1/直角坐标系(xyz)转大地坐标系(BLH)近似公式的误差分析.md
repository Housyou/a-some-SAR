> $arctan$函数与$arctan2$函数的转换关系
> $$arctan2(y,x) = \begin{cases}  
arctan(\frac{y}{x}) & x\gt0\\
arctan(\frac{y}{x})+\pi & y\ge0,x\lt0\\
arctan(\frac{y}{x})-\pi & y\lt0,x\lt0\\
\frac{\pi}{2} & y\gt0,x=0\\
-\frac{\pi}{2} & y\lt0,x=0\\
undefined & y=0,x=0
\end{cases}$$
```python
import matplotlib.pyplot as plt
import numpy as np

start, end, num = -1, 1, 100
var = np.linspace(start, end, num + 1)  # 变量区间[-1,1]，在这之中取101个数
x, y = np.meshgrid(var, var)
# x, y的shape都是(101,101)，表示这101x101个点的二维坐标
axes = (plt.subplot(1, 2, 1), plt.subplot(1, 2, 2))
z = (np.arctan(y / x) / np.pi, np.arctan2(y, x) / np.pi)
titles = ('arctan(y/x)', 'arctan2(y,x)')
for i, j, k in zip(axes, z, titles):
    ai = i.imshow(j, cmap='gray')
    i.set_ylim(0, num)  # y轴方向调整为朝上
    i.set_xticks([0, num])  # 因为有101个点，所以取值范围是[0,100]
    i.set_xticklabels([start, end])  # 把取值还原回[-1,1]
    i.set_xlabel('x')
    i.set_yticks([0, num])
    i.set_yticklabels([start, end])
    i.set_ylabel('y')
    i.set_title(k)
colorbar = plt.colorbar(ai, ax=axes)  # 共用一个colorbar
colorbar.set_ticks([-0.99, -0.5, 0, 0.5, 1])
colorbar.set_ticklabels(
    [r'$-0.99\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
plt.show()
```
