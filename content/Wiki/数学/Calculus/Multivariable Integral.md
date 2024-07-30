# 多元积分 Multivariable Integral

## 概念与定义 Concepts and Definitions

### 二重积分 Double Integral

对于一个定义在闭区域 $D$ 上的连续函数 $f(x, y)$，二重积分表示为：

$$
\iint_D f(x, y) \, dA
$$

其中 $dA$ 表示微小区域元。二重积分可以看作是在区域 $D$ 上对函数 $f(x, y)$ 进行累积求和

For a continuous function $f(x, y)$ defined over a closed region $D$, the double integral is denoted as:

$$
\iint_D f(x, y) \, dA
$$

where $dA$ represents a small area element. The double integral can be considered as the accumulated sum of the function $f(x, y)$ over the region $D$

### 三重积分 Triple Integral

对于一个定义在闭区域 $V$ 上的连续函数 $f(x, y, z)$，三重积分表示为：

$$
\iiint_V f(x, y, z) \, dV
$$

其中 $dV$ 表示微小体积元。三重积分可以看作是在体积 $V$ 上对函数 $f(x, y, z)$ 进行累积求和

For a continuous function $f(x, y, z)$ defined over a closed region $V$, the triple integral is denoted as:

$$
\iiint_V f(x, y, z) \, dV
$$

where $dV$ represents a small volume element. The triple integral can be considered as the accumulated sum of the function $f(x, y, z)$ over the volume $V$

## 性质与定理 Properties and Theorems

### 迭代积分 Iterated Integrals

二重积分可以通过迭代积分来计算。假设区域 $D$ 由 $x$ 轴上的 $a$ 到 $b$ 和 $y$ 轴上的 $c$ 到 $d$ 界定，则二重积分可以表示为：

$$
\iint_D f(x, y) \, dA = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx
$$

或者

$$
\iint_D f(x, y) \, dA = \int_c^d \left( \int_a^b f(x, y) \, dx \right) dy
$$

The double integral can be computed using iterated integrals. Suppose the region $D$ is bounded by $a$ to $b$ on the $x$-axis and $c$ to $d$ on the $y$-axis, then the double integral can be expressed as:

$$
\iint_D f(x, y) \, dA = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx
$$

or

$$
\iint_D f(x, y) \, dA = \int_c^d \left( \int_a^b f(x, y) \, dx \right) dy
$$

同理，三重积分可以表示为：

$$
\iiint_V f(x, y, z) \, dV = \int_a^b \left( \int_c^d \left( \int_e^f f(x, y, z) \, dz \right) dy \right) dx
$$

Similarly, the triple integral can be expressed as:

$$
\iiint_V f(x, y, z) \, dV = \int_a^b \left( \int_c^d \left( \int_e^f f(x, y, z) \, dz \right) dy \right) dx
$$

### 变量替换法 Change of Variables

#### Jacobi 行列式 Jacobi Determinant

在多元积分中，当进行变量替换时，Jacobi 行列式（Jacobian Determinant）是非常重要的工具。设有一组变量 $(u_1, u_2, \ldots, u_n)$ 和 $(x_1, x_2, \ldots, x_n)$，变量之间的关系为：

$$
x_i = x_i(u_1, u_2, \ldots, u_n) \quad \text{for } i = 1, 2, \ldots, n
$$

Jacobi 行列式定义为以下偏导数行列式：

$$
J = \frac{\partial(x_1, x_2, \ldots, x_n)}{\partial(u_1, u_2, \ldots, u_n)} = 
\begin{vmatrix}
\frac{\partial x_1}{\partial u_1} & \frac{\partial x_1}{\partial u_2} & \cdots & \frac{\partial x_1}{\partial u_n} \\
\frac{\partial x_2}{\partial u_1} & \frac{\partial x_2}{\partial u_2} & \cdots & \frac{\partial x_2}{\partial u_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial x_3}{\partial u_1} & \frac{\partial x_3}{\partial u_2} & \cdots & \frac{\partial x_3}{\partial u_n}
\end{vmatrix}
$$

In multiple integrals, when performing variable substitution, the Jacobi determinant (Jacobian Determinant) is a crucial tool. Given a set of variables $(u_1, u_2, \ldots, u_n)$ and $(x_1, x_2, \ldots, x_n)$, with the relationships:

$$
x_i = x_i(u_1, u_2, \ldots, u_n) \quad \text{for } i = 1, 2, \ldots, n
$$

The Jacobi determinant is defined as the determinant of the following partial derivatives:

$$
J = \frac{\partial(x_1, x_2, \ldots, x_n)}{\partial(u_1, u_2, \ldots, u_n)} = 
\begin{vmatrix}
\frac{\partial x_1}{\partial u_1} & \frac{\partial x_1}{\partial u_2} & \cdots & \frac{\partial x_1}{\partial u_n} \\
\frac{\partial x_2}{\partial u_1} & \frac{\partial x_2}{\partial u_2} & \cdots & \frac{\partial x_2}{\partial u_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial x_3}{\partial u_1} & \frac{\partial x_3}{\partial u_2} & \cdots & \frac{\partial x_3}{\partial u_n}
\end{vmatrix}
$$

#### Jacobi 行列式在多元积分中的应用 Applications of the Jacobi Determinant in Multiple Integrals

在进行变量替换时，积分区域和被积函数都会随之改变。设原积分变量为 $(x_1, x_2, \ldots, x_n)$，替换后的变量为 $(u_1, u_2, \ldots, u_n)$，原积分区域为 $D$，替换后的积分区域为 $D'$。则有以下关系：

$$
dV = \left| J \right| \, dU
$$

其中 $\left| J \right|$ 表示 Jacobi 行列式的绝对值。对于多重积分，我们有：

$$
\iiint_D f(x_1, x_2, x_3) \, dV = \iiint_{D'} f(x_1(u_1, u_2, u_3), x_2(u_1, u_2, u_3), x_3(u_1, u_2, u_3)) \left| J \right| \, dU
$$

When performing variable substitution, both the integration region and the integrand change accordingly. Let the original integration variables be $(x_1, x_2, \ldots, x_n)$ and the substituted variables be $(u_1, u_2, \ldots, u_n)$. The original integration region is $D$ and the substituted integration region is $D'$. The relationship is given by:

$$
dV = \left| J \right| \, dU
$$

where $\left| J \right|$ represents the absolute value of the Jacobi determinant. For multiple integrals, we have:

$$
\iiint_D f(x_1, x_2, x_3) \, dV = \iiint_{D'} f(x_1(u_1, u_2, u_3), x_2(u_1, u_2, u_3), x_3(u_1, u_2, u_3)) \left| J \right| \, dU
$$

#### 变量替换及其 Jacobi 行列式 Variable Substitution and Its Jacobi Determinant

##### 极坐标 Polar Coordinates

对于二重积分，如果积分区域 $D$ 是圆形或部分圆形，可以将直角坐标系 $(x, y)$ 换成极坐标系 $(r, \theta)$，转换关系为：

$$
x = r \cos \theta \\
y = r \sin \theta \\
dA = r \, dr \, d\theta
$$

Jacobi 行列式为：

$$
J = \left| \frac{\partial(x, y)}{\partial(r, \theta)} \right| = \left| \begin{vmatrix}
\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\
\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta}
\end{vmatrix} \right| = \left| \begin{vmatrix}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{vmatrix} \right| = r
$$

二重积分表示为：

$$
\iint_D f(x, y) \, dA = \iint_{D'} f(r \cos \theta, r \sin \theta) \, r \, dr \, d\theta
$$

For double integrals, if the integration region $D$ is circular or partially circular, Cartesian coordinates $(x, y)$ can be changed to polar coordinates $(r, \theta)$. The transformation relations are:

$$
x = r \cos \theta \\
y = r \sin \theta \\
dA = r \, dr \, d\theta
$$

The Jacobi determinant is:

$$
J = \left| \frac{\partial(x, y)}{\partial(r, \theta)} \right| = \left| \begin{vmatrix}
\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\
\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta}
\end{vmatrix} \right| = \left| \begin{vmatrix}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{vmatrix} \right| = r
$$

The double integral is expressed as:

$$
\iint_D f(x, y) \, dA = \iint_{D'} f(r \cos \theta, r \sin \theta) \, r \, dr \, d\theta
$$

##### 柱坐标 Cylindrical Coordinates

对于三重积分，如果积分区域 $V$ 是圆柱形，可以将直角坐标系 $(x, y, z)$ 换成柱坐标系 $(r, \theta, z)$，转换关系为：

$$
x = r \cos \theta \\
y = r \sin \theta \\
z = z \\
dV = r \, dr \, d\theta \, dz
$$

Jacobi 行列式为：

$$
J = \left| \frac{\partial(x, y, z)}{\partial(r, \theta, z)} \right| = \left| \begin{vmatrix}
\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} & \frac{\partial x}{\partial z} \\
\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} & \frac{\partial y}{\partial z} \\
\frac{\partial z}{\partial r} & \frac{\partial z}{\partial \theta} & \frac{\partial z}{\partial z}
\end{vmatrix} \right| = \left| \begin{vmatrix}
\cos \theta & -r \sin \theta & 0 \\
\sin \theta & r \cos \theta & 0 \\
0 & 0 & 1
\end{vmatrix} \right| = r
$$

三重积分表示为：

$$
\iiint_V f(x, y, z) \, dV = \iiint_{V'} f(r \cos \theta, r \sin \theta, z) \, r \, dr \, d\theta \, dz
$$

For triple integrals, if the integration region $V$ is cylindrical, Cartesian coordinates $(x, y, z)$ can be changed to cylindrical coordinates $(r, \theta, z)$. The transformation relations are:

$$
x = r \cos \theta \\
y = r \sin \theta \\
z = z \\
dV = r \, dr \, d\theta \, dz
$$

The Jacobi determinant is:

$$
J = \left| \frac{\partial(x, y, z)}{\partial(r, \theta, z)} \right| = \left| \begin{vmatrix}
\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} & \frac{\partial x}{\partial z} \\
\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} & \frac{\partial y}{\partial z} \\
\frac{\partial z}{\partial r} & \frac{\partial z}{\partial \theta} & \frac{\partial z}{\partial z}
\end{vmatrix} \right| = \left| \begin{vmatrix}
\cos \theta & -r \sin \theta & 0 \\
\sin \theta & r \cos \theta & 0 \\
0 & 0 & 1
\end{vmatrix} \right| = r
$$

The triple integral is expressed as:

$$
\iiint_V f(x, y, z) \, dV = \iiint_{V'} f(r \cos \theta, r \sin \theta, z) \, r \, dr \, d\theta \, dz
$$

##### 球坐标 Spherical Coordinates

对于三重积分，如果积分区域 $V$ 是球形，可以将直角坐标系 $(x, y, z)$ 换成球坐标系 $(\rho, \theta, \phi)$，转换关系为：

$$
x = \rho \sin \phi \cos \theta \\
y = \rho \sin \phi \sin \theta \\
z = \rho \cos \phi \\
dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

Jacobi 行列式为：

$$
J = \left| \frac{\partial(x, y, z)}{\partial(\rho, \theta, \phi)} \right| = \left| \begin{vmatrix}
\frac{\partial x}{\partial \rho} & \frac{\partial x}{\partial \theta} & \frac{\partial x}{\partial \phi} \\
\frac{\partial y}{\partial \rho} & \frac{\partial y}{\partial \theta} & \frac{\partial y}{\partial \phi} \\
\frac{\partial z}{\partial \rho} & \frac{\partial z}{\partial \theta} & \frac{\partial z}{\partial \phi}
\end{vmatrix} \right| = \left| \begin{vmatrix}
\sin \phi \cos \theta & -\rho \sin \phi \sin \theta & \rho \cos \phi \cos \theta \\
\sin \phi \sin \theta & \rho \sin \phi \cos \theta & \rho \cos \phi \sin \theta \\
\cos \phi & 0 & -\rho \sin \phi
\end{vmatrix} \right| = \rho^2 \sin \phi
$$

三重积分表示为：

$$
\iiint_V f(x, y, z) \, dV = \iiint_{V'} f(\rho \sin \phi \cos \theta, \rho \sin \phi \sin \theta, \rho \cos \phi) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

For triple integrals, if the integration region $V$ is spherical, Cartesian coordinates $(x, y, z)$ can be changed to spherical coordinates $(\rho, \theta, \phi)$. The transformation relations are:

$$
x = \rho \sin \phi \cos \theta \\
y = \rho \sin \phi \sin \theta \\
z = \rho \cos \phi \\
dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

The Jacobi determinant is:

$$
J = \left| \frac{\partial(x, y, z)}{\partial(\rho, \theta, \phi)} \right| = \left| \begin{vmatrix}
\frac{\partial x}{\partial \rho} & \frac{\partial x}{\partial \theta} & \frac{\partial x}{\partial \phi} \\
\frac{\partial y}{\partial \rho} & \frac{\partial y}{\partial \theta} & \frac{\partial y}{\partial \phi} \\
\frac{\partial z}{\partial \rho} & \frac{\partial z}{\partial \theta} & \frac{\partial z}{\partial \phi}
\end{vmatrix} \right| = \left| \begin{vmatrix}
\sin \phi \cos \theta & -\rho \sin \phi \sin \theta & \rho \cos \phi \cos \theta \\
\sin \phi \sin \theta & \rho \sin \phi \cos \theta & \rho \cos \phi \sin \theta \\
\cos \phi & 0 & -\rho \sin \phi
\end{vmatrix} \right| = \rho^2 \sin \phi
$$

The triple integral is expressed as:

$$
\iiint_V f(x, y, z) \, dV = \iiint_{V'} f(\rho \sin \phi \cos \theta, \rho \sin \phi \sin \theta, \rho \cos \phi) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

## 计算技巧 Calculation Techniques

### 判断积分区域 Determining the Integration Region

#### 二重积分区域 Double Integral Region

常见的二重积分区域有矩形区域和一般区域。对于一般区域，可以根据边界曲线确定积分区域：

$$
D = \{(x, y) \mid a \le x \le b, g_1(x) \le y \le g_2(x) \}
$$

此时，二重积分表示为：

$$
\iint_D f(x, y) \, dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \right) dx
$$

Common double integral regions include rectangular regions and general regions. For a general region, the integration region can be determined by boundary curves:

$$
D = \{(x

, y) \mid a \le x \le b, g_1(x) \le y \le g_2(x) \}
$$

At this time, the double integral is expressed as:

$$
\iint_D f(x, y) \, dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \right) dx
$$

#### 三重积分区域 Triple Integral Region

常见的三重积分区域有矩形区域和一般区域。对于一般区域，可以根据边界曲面确定积分区域：

$$
V = \{(x, y, z) \mid a \le x \le b, g_1(x) \le y \le g_2(x), h_1(x, y) \le z \le h_2(x, y) \}
$$

此时，三重积分表示为：

$$
\iiint_V f(x, y, z) \, dV = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} \left( \int_{h_1(x, y)}^{h_2(x, y)} f(x, y, z) \, dz \right) dy \right) dx
$$

Common triple integral regions include rectangular regions and general regions. For a general region, the integration region can be determined by boundary surfaces:

$$
V = \{(x, y, z) \mid a \le x \le b, g_1(x) \le y \le g_2(x), h_1(x, y) \le z \le h_2(x, y) \}
$$

At this time, the triple integral is expressed as:

$$
\iiint_V f(x, y, z) \, dV = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} \left( \int_{h_1(x, y)}^{h_2(x, y)} f(x, y, z) \, dz \right) dy \right) dx
$$

### 常见积分区域换元技巧 Common Transformation Techniques for Integration Regions

#### 圆区域 Circular Region

当积分区域为圆或部分圆时，使用极坐标变换，将积分区域从 $(x, y)$ 变换到 $(r, \theta)$，并使用 $dA = r \, dr \, d\theta$

When the integration region is a circle or part of a circle, use the polar coordinate transformation to change the integration region from $(x, y)$ to $(r, \theta)$, and use $dA = r \, dr \, d\theta$

#### 柱形区域 Cylindrical Region

当积分区域为柱形时，使用柱坐标变换，将积分区域从 $(x, y, z)$ 变换到 $(r, \theta, z)$，并使用 $dV = r \, dr \, d\theta \, dz$

When the integration region is cylindrical, use the cylindrical coordinate transformation to change the integration region from $(x, y, z)$ to $(r, \theta, z)$, and use $dV = r \, dr \, d\theta \, dz$

#### 球形区域 Spherical Region

当积分区域为球形时，使用球坐标变换，将积分区域从 $(x, y, z)$ 变换到 $(\rho, \theta, \phi)$，并使用 $dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$

When the integration region is spherical, use the spherical coordinate transformation to change the integration region from $(x, y, z)$ to $(\rho, \theta, \phi)$, and use $dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta$

## 例题 Examples

### 例 1 Example 1

计算二重积分 $\iint_D (x^2 + y^2) \, dA$，其中区域 $D$ 是单位圆 $x^2 + y^2 \le 1$

Calculate the double integral $\iint_D (x^2 + y^2) \, dA$ where the region $D$ is the unit circle $x^2 + y^2 \le 1$

解：

使用极坐标变换：

$$
x = r \cos \theta \\
y = r \sin \theta \\
dA = r \, dr \, d\theta
$$

积分区域 $D$ 变为 $0 \le r \le 1, 0 \le \theta \le 2\pi$

$$
\iint_D (x^2 + y^2) \, dA = \int_0^{2\pi} \int_0^1 (r^2) \, r \, dr \, d\theta \\
= \int_0^{2\pi} \int_0^1 r^3 \, dr \, d\theta \\
= \int_0^{2\pi} \left[ \frac{r^4}{4} \right]_0^1 \, d\theta \\
= \int_0^{2\pi} \frac{1}{4} \, d\theta \\
= \frac{1}{4} \cdot 2\pi \\
= \frac{\pi}{2}
$$

Solution:

Using the polar coordinate transformation:

$$
x = r \cos \theta \\
y = r \sin \theta \\
dA = r \, dr \, d\theta
$$

The integration region $D$ becomes $0 \le r \le 1, 0 \le \theta \le 2\pi$

$$
\iint_D (x^2 + y^2) \, dA = \int_0^{2\pi} \int_0^1 (r^2) \, r \, dr \, d\theta \\
= \int_0^{2\pi} \int_0^1 r^3 \, dr \, d\theta \\
= \int_0^{2\pi} \left[ \frac{r^4}{4} \right]_0^1 \, d\theta \\
= \int_0^{2\pi} \frac{1}{4} \, d\theta \\
= \frac{1}{4} \cdot 2\pi \\
= \frac{\pi}{2}
$$

### 例 2 Example 2

计算三重积分 $\iiint_V (x^2 + y^2 + z^2) \, dV$，其中区域 $V$ 是单位球 $x^2 + y^2 + z^2 \le 1$

Calculate the triple integral $\iiint_V (x^2 + y^2 + z^2) \, dV$ where the region $V$ is the unit sphere $x^2 + y^2 + z^2 \le 1$

解：

使用球坐标变换：

$$
x = \rho \sin \phi \cos \theta \\
y = \rho \sin \phi \sin \theta \\
z = \rho \cos \phi \\
dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

积分区域 $V$ 变为 $0 \le \rho \le 1, 0 \le \phi \le \pi, 0 \le \theta \le 2\pi$

$$
\iiint_V (x^2 + y^2 + z^2) \, dV = \iiint_{V'} (\rho^2) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta \\
= \int_0^{2\pi} \int_0^\pi \int_0^1 \rho^4 \sin \phi \, d\rho \, d\phi \, d\theta \\
= \int_0^{2\pi} \int_0^\pi \left[ \frac{\rho^5}{5} \right]_0^1 \sin \phi \, d\phi \, d\theta \\
= \int_0^{2\pi} \int_0^\pi \frac{1}{5} \sin \phi \, d\phi \, d\theta \\
= \frac{1}{5} \int_0^{2\pi} \left[ -\cos \phi \right]_0^\pi \, d\theta \\
= \frac{1}{5} \int_0^{2\pi} (2) \, d\theta \\
= \frac{2}{5} \cdot 2\pi \\
= \frac{4\pi}{5}
$$

Solution:

Using the spherical coordinate transformation:

$$
x = \rho \sin \phi \cos \theta \\
y = \rho \sin \phi \sin \theta \\
z = \rho \cos \phi \\
dV = \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta
$$

The integration region $V$ becomes $0 \le \rho \le 1, 0 \le \phi \le \pi, 0 \le \theta \le 2\pi$

$$
\iiint_V (x^2 + y^2 + z^2) \, dV = \iiint_{V'} (\rho^2) \, \rho^2 \sin \phi \, d\rho \, d\phi \, d\theta \\
= \int_0^{2\pi} \int_0^\pi \int_0^1 \rho^4 \sin \phi \, d\rho \, d\phi \, d\theta \\
= \int_0^{2\pi} \int_0^\pi \left[ \frac{\rho^5}{5} \right]_0^1 \sin \phi \, d\phi \, d\theta \\
= \int_0^{2\pi} \int_0^\pi \frac{1}{5} \sin \phi \, d\phi \, d\theta \\
= \frac{1}{5} \int_0^{2\pi} \left[ -\cos \phi \right]_0^\pi \, d\theta \\
= \frac{1}{5} \int_0^{2\pi} (2) \, d\theta \\
= \frac{2}{5} \cdot 2\pi \\
= \frac{4\pi}{5}
$$
