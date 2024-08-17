# 常微分方程考前速查表

## 1. 基本概念

### 1.1 常微分方程的阶

方程中最高阶导数的阶数

### 1.2 解的类型

- 通解：包含任意常数的解
- 特解：不包含任意常数的解
- 隐式解：以隐函数形式给出的解
- 奇解：不能从通解得到的解

## 2. 一阶常微分方程

### 2.1 可分离变量方程

形如：$\frac{dy}{dx} = f(x)g(y)$

解法：$\int \frac{dy}{g(y)} = \int f(x)dx + C$

### 2.2 齐次方程

形如：$\frac{dy}{dx} = f(\frac{y}{x})$

解法：令 $u = \frac{y}{x}$，则 $y = ux$，$\frac{dy}{dx} = u + x\frac{du}{dx}$

### 2.3 一阶线性方程

形如：$\frac{dy}{dx} + P(x)y = Q(x)$

解法：积分因子法，$\mu(x) = e^{\int P(x)dx}$

### 2.4 Bernoulli 方程

形如：$\frac{dy}{dx} + P(x)y = Q(x)y^n, n \neq 0,1$

解法：令 $u = y^{1-n}$，转化为线性方程

### 2.5 全微分方程

形如：$M(x,y)dx + N(x,y)dy = 0$

条件：$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$

解法：$\int M dx + \int (N - \int \frac{\partial M}{\partial y} dx) dy = C$

### 2.6 一阶隐式方程

形如：$F(x,y,\frac{dy}{dx}) = 0$

解法：

1. 参数化：令 $\frac{dy}{dx} = p$，解 $F(x,y,p) = 0$
2. 包络法：消去参数 $p$

## 3. 高阶常微分方程

### 3.1 可降阶方程

1. $y^{(n)} = f(x)$：直接积分 $n$ 次
2. $y'' = f(x,y')$：令 $p = y'$，转化为一阶方程
3. $y'' = f(y,y')$：令 $p = y'$，$\frac{d^2y}{dx^2} = p\frac{dp}{dy}$

### 3.2 线性微分方程

形如：$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \cdots + a_1(x)y' + a_0(x)y = f(x)$

#### 3.2.1 齐次线性方程

当 $f(x) = 0$ 时：

- 通解：$y = c_1y_1 + c_2y_2 + \cdots + c_ny_n$
- 线性无关解的判别：Wronskian 行列式 $W(y_1,\ldots,y_n) \neq 0$

#### 3.2.2 非齐次线性方程

解法：

1. 常数变易法
2. 特解叠加原理

### 3.3 欧拉方程

形如：$x^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)$

解法：令 $x = e^t$，转化为常系数线性方程

## 4. 常系数线性微分方程

### 4.1 齐次方程

形如：$a_ny^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1y' + a_0y = 0$

特征方程：$a_n\lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_1\lambda + a_0 = 0$

解的形式：

1. 单根 $\lambda_i$：$y_i = e^{\lambda_i x}$
2. $k$ 重根 $\lambda_i$：$y_i = x^j e^{\lambda_i x}, j = 0,1,\ldots,k-1$
3. 共轭复根 $a \pm bi$：$y_1 = e^{ax}\cos bx, y_2 = e^{ax}\sin bx$

### 4.2 非齐次方程

形如：$a_ny^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1y' + a_0y = f(x)$

特解形式：

1. $f(x) = P_m(x)e^{\alpha x}$：$y_p = x^k Q_m(x)e^{\alpha x}$
   - $k = 0$ 如果 $\alpha$ 不是特征根
   - $k$ 等于 $\alpha$ 作为特征根的重数
2. $f(x) = e^{\alpha x}[P_l(x)\cos \beta x + P_m(x)\sin \beta x]$：
   $y_p = x^k e^{\alpha x}[Q_l(x)\cos \beta x + Q_m(x)\sin \beta x]$
   - $k = 0$ 如果 $\alpha \pm \beta i$ 不是特征根
   - $k = 1$ 如果 $\alpha \pm \beta i$ 是特征根

## 5. 微分方程组

### 5.1 一阶线性系统

形如：$\mathbf{x}' = A(t)\mathbf{x} + \mathbf{b}(t)$

解法：

1. 特征值法（当 $A$ 为常数矩阵）
2. 矩阵指数法：$\mathbf{x} = e^{At}\mathbf{c} + \int_0^t e^{A(t-s)}\mathbf{b}(s)ds$

### 5.2 高阶方程转化为一阶系统

令 $x_1 = y, x_2 = y', \ldots, x_n = y^{(n-1)}$

## 6. 边值问题

### 6.1 Sturm-Liouville 问题

形如：$-(p(x)y')' + q(x)y = \lambda r(x)y$

边界条件：$\alpha_1 y(a) + \alpha_2 y'(a) = 0$, $\beta_1 y(b) + \beta_2 y'(b) = 0$

性质：

1. 特征值都是实数
2. 不同特征值对应的特征函数正交

### 6.2 Green 函数

用于求解非齐次边值问题：$Ly = f(x)$，$y(a) = y(b) = 0$

解：$y(x) = \int_a^b G(x,\xi)f(\xi)d\xi$

## 7. 级数解法

### 7.1 幂级数解

假设解的形式：$y = \sum_{n=0}^{\infty} a_n x^n$

### 7.2 Frobenius 方法

用于奇点处的解，假设解的形式：$y = x^r \sum_{n=0}^{\infty} a_n x^n$

## 重点难点提示

- 熟练掌握一阶方程的各种解法，特别是可分离变量和线性方程
- 理解线性方程的结构，包括齐次和非齐次的解法
- 掌握常系数线性方程的特征方程方法
- 对于非齐次方程，重点关注特解的构造方法
- 理解微分方程组和高阶方程之间的转化
- 了解边值问题和级数解法的基本思想
