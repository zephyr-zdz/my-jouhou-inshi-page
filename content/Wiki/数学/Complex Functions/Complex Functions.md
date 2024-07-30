# 复变函数 Complex Functions

## 指数形式 Exponential Form

### 定义 Definition

复数 $z$ 可以表示为指数形式：
A complex number $z$ can be expressed in exponential form:

$$
z = re^{i\theta}
$$

其中 $r$ 是模，$\theta$ 是辐角
where $r} is the modulus, and $\theta$ is the argument

### 复数的模和辐角 Modulus and Argument of a Complex Number

1. 模 $r$ 计算方法：
Modulus $r$ calculation:

$$
r = |z| = \sqrt{x^2 + y^2}
$$

2. 辐角 $\theta$ 计算方法：
Argument $\theta$ calculation:

$$
\theta = \arg(z) = \tan^{-1}\left(\frac{y}{x}\right)
$$

### 欧拉公式 Euler's Formula

欧拉公式：
Euler's formula:

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta)
$$

利用欧拉公式，复数 $z = re^{i\theta}$ 可以写成：
Using Euler's formula, a complex number $z = re^{i\theta}$ can be written as:

$$
z = r(\cos(\theta) + i\sin(\theta))
$$

### 三角函数和 $a + bi$ 形式的转化 Conversion between Trigonometric and $a + bi$ Forms

复数 $z = re^{i\theta}$ 可以转化为 $a + bi$ 形式：
A complex number $z = re^{i\theta}$ can be converted to $a + bi$ form:

$$
a = r\cos(\theta)
$$

$$
b = r\sin(\theta)
$$

因此：
Therefore:

$$
z = a + bi = r\cos(\theta) + ir\sin(\theta)
$$

### 复数的实部和虚部 Real and Imaginary Parts of a Complex Number

从指数形式 $z = re^{i\theta}$ 中，实部和虚部的计算方法：
From the exponential form $z = re^{i\theta}$, the real and imaginary parts can be calculated as follows:

$$
\Re(z) = r\cos(\theta)
$$

$$
\Im(z) = r\sin(\theta)
$$

### 复数乘法 Multiplication of Complex Numbers

复数 $z_1 = r_1 e^{i\theta_1}$ 和 $z_2 = r_2 e^{i\theta_2}$ 相乘：
Multiplication of complex numbers $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$:

$$
z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)}
$$

### 复数除法 Division of Complex Numbers

复数 $z_1 = r_1 e^{i\theta_1}$ 和 $z_2 = r_2 e^{i\theta_2}$ 相除：
Division of complex numbers $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$:

$$
\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}
$$

### 复数的幂 Powers of Complex Numbers

复数 $z = re^{i\theta}$ 的 $n$ 次幂：
The $n$-th power of a complex number $z = re^{i\theta}$:

$$
z^n = \left(re^{i\theta}\right)^n = r^n e^{in\theta}
$$

### 复数的根 Roots of Complex Numbers

复数 $z = re^{i\theta}$ 的 $n$ 次方根：
The $n$-th root of a complex number $z = re^{i\theta}$:

$$
z^{1/n} = \left(re^{i\theta}\right)^{1/n} = r^{1/n} e^{i\left(\theta + 2k\pi\right)/n}
$$

其中 $k = 0, 1, 2, \ldots, n-1
where $k = 0, 1, 2, \ldots, n-1

### 复数的共轭 Conjugate of a Complex Number

复数 $z = re^{i\theta}$ 的共轭 $z^*$ 是：
The conjugate of a complex number $z = re^{i\theta}$ is:

$$
z^* = re^{-i\theta}
$$

### 共轭性质 Properties of Conjugate

1. 共轭的模不变：
The modulus of the conjugate remains the same:

$$
|z^*| = |z| = r
$$

2. 共轭的辐角取反：
The argument of the conjugate is negated:

$$
\arg(z^*) = -\arg(z)
$$

3. 共轭运算的可逆性：
Conjugation is an involution:

$$
(z^*)^* = z
$$

4. 加法中的共轭：
Conjugate in addition:

$$
(z_1 + z_2)^* = z_1^* + z_2^*
$$

5. 乘法中的共轭：
Conjugate in multiplication:

$$
(z_1 z_2)^* = z_1^* z_2^*
$$

6. 商的共轭：
Conjugate of a quotient:

$$
\left(\frac{z_1}{z_2}\right)^* = \frac{z_1^*}{z_2^*}
$$

### 共轭的应用 Applications of Conjugate

1. 计算复数的模：
Calculate the modulus of a complex number:

$$
|z| = \sqrt{z z^*}
$$

2. 求复数的实部和虚部：
Find the real and imaginary parts of a complex number:

$$
\Re(z) = \frac{z + z^*}{2}
$$

$$
\Im(z) = \frac{z - z^*}{2i}
$$

### 常见问题及注意事项 Common Issues and Tips

1. 计算辐角时，注意区分象限，使用 $\tan^{-1}$ 的正确象限
When calculating the argument, be careful to distinguish the quadrant and use the correct quadrant for $\tan^{-1}$

2. 辐角范围通常取 $(-\pi, \pi]$ 或 $[0, 2\pi)$
The argument range is usually taken as $(-\pi, \pi]$ or $[0, 2\pi)$

3. 复数的指数形式运算在处理乘法、除法和求幂时尤其方便
The exponential form of complex numbers is especially convenient for multiplication, division, and exponentiation

### 复数的根和单位根 Roots and Roots of Unity

复数 $z$ 的 $n$ 次方根是使 $z^n = 1$ 的所有复数。
The $n$-th roots of unity are all complex numbers such that $z^n = 1$.

这些根可以表示为：
These roots can be expressed as:

$$
\omega_k = e^{i\frac{2k\pi}{n}}, \quad k = 0, 1, 2, \ldots, n-1
$$

### 单位根的性质 Properties of Roots of Unity

1. 单位根的和为零：
The sum of the $n$-th roots of unity is zero:

$$
\sum_{k=0}^{n-1} \omega_k = 0
$$

2. 单位根是等间隔分布在单位圆上的点：
The roots of unity are equally spaced points on the unit circle in the complex plane.

3. 单位根满足 $\omega_k^n = 1$：
Each root of unity satisfies $\omega_k^n = 1$.

### 单位根的应用 Applications of Roots of Unity

单位根在傅里叶变换和数值分析中有广泛应用。
Roots of unity have wide applications in Fourier transforms and numerical analysis.
