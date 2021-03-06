![title](https://raw.githubusercontent.com/Housyou/SAR/master/origin%20ver/a0/imgs/1.png)
# 天线中的口径面积-波束范围(Aperture-beam-area)的关系

约翰·克劳斯(John D.Kraus)等编著的《天线》（第三版）第2章-天线基础 2.9节-天线口径 公式(5)-口径面积-波束范围(Aperture-beam-area)的关系式
$$\lambda^2=A_e\Omega_A$$
推导过程中使用了公式
$$E_r=\frac{E_aA_e}{r\lambda}$$
却没有给出公式推导，这让数理基础薄弱的我非常困扰。查了一圈网上好像有人有同样的疑惑，所以在这里把原理简单的记录一下。

>假设有一个有效口径为 $A_e$ 的天线，将其全部功率按一波束范围为 $\Omega_A(sr)$ 的圆锥形波瓣辐射，如图所示。若口径上有均匀场 $E_a$，则其辐射功率为
>$$P=\frac{E_a^2}{Z_0}A_e\quad(W)$$
>式中$Z_0$为媒质的本征阻抗（在空气或真空中为377 $\Omega$ ）。
![photo](https://raw.githubusercontent.com/Housyou/SAR/master/origin%20ver/a0/imgs/2.png)

假定在距离为 $r$ 处有均匀的远场 $E$，则辐射功率还可写成
$$P=\frac{E_r^2}{Z_0}r^2\Omega_A\quad (W)$$
这个很好理解，就是用 $r^2\Omega_A$ 取代有效口径 $A_e$ 得到的公式。两式联立得到
$$E_r^2=E_a^2\frac{A_e}{r^2\Omega_A}$$
然后是 $E_r=\frac{E_aA_e}{r\lambda}$ 的由来：

>**惠更斯-菲涅尔原理**
>$$\tilde E_r=K\iint_\Sigma f(\theta_0,\theta)\tilde E_a\frac{e^{ikr}}{r}dS$$
>公式基于物理上的基本事实：  
>1. $\tilde E_r\propto f(\theta_0,\theta)$ 倾斜因子表示次波面源的发射非各向同性
>2. $\tilde E_r\propto \tilde E_a$ 次波源的自身复振幅 
>3. $\tilde E_r\propto \frac{e^{ikr}}{r}$ 次波源发出的球面波到达场点
>4. $\tilde E_r\propto dS$ 波前上作为次波源的微分面源

![photo](https://raw.githubusercontent.com/Housyou/SAR/master/origin%20ver/a0/imgs/3.png)

>**基尔霍夫衍射积分公式**
>$$\tilde E_r=\frac{-i}{\lambda}\iint_\Sigma \frac{cos\theta_0+cos\theta}{2}\tilde E_a\frac{e^{ikr}}{r}dS$$
>1. 明确了倾斜因子，$f(\theta_0,\theta)=\frac{cos\theta_0+cos\theta}{2}$
>2. 给出了比例系数，$K=\frac{-i}{\lambda}=\frac{1}{\lambda}e^{-i\frac{\pi}{2}}$
>3. 明确指出，积分面$(\Sigma)$不限于等相面，可以是隔离光源和场点的任意闭合曲面。

根据示意图，或者说简化考虑，$\theta=\theta_0=0$，此处仅考虑振幅不考虑相位，故
$$E_r=\frac{1}{\lambda}\frac{1+1}{2}E_a\frac{1}{r}A_e=\frac{E_aA_e}{r\lambda}$$
$$E_r^2=\frac{E_a^2A_e^2}{r^2\lambda^2}$$
显然
$$\frac{1}{\Omega_A}=\frac{A_e}{\lambda^2}$$
$$\lambda^2=A_e\Omega_A$$
最后说说我的理解。$\lambda^2$ 这一项是定值一般无法改变，所以认为口径面积 $A_e$ 与波束范围 $\Omega_A$ 成反比。这很像侧视雷达中天线长度 $L$ 与半功率波束宽度 $\beta$ 的关系：
$$\beta=0.88\frac{\lambda}{L}$$
$L$ 越大波束便越定向，$\beta$ 越小，合成孔径雷达的方位向分辨率越好。口径面积 $A_e$、天线长度 $L$ 的增加意味着更多的电磁波进行叠加，只有在法线方向上所有电磁波都没有相位差，可以代数相加，该方向的振幅得到极大增强，波束的定向性也增强。