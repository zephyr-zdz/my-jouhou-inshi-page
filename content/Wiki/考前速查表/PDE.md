# 偏微分方程考前速查表

## 1. 基本概念

### 1.1 偏微分方程的阶

方程中最高阶偏导数的阶数

### 1.2 线性和非线性

线性 PDE：形如 $a_1u_{xx} + a_2u_{yy} + a_3u_x + a_4u_y + a_5u = f(x,y)$

### 1.3 齐次性

齐次 PDE：右端项 $f(x,y) = 0$

## 2. PDE 的分类

### 2.1 二阶线性 PDE 的分类

$au_{xx} + 2bu_{xy} + cu_{yy} + du_x + eu_y + fu = g$

- 双曲型：$b^2 - ac > 0$
- 抛物型：$b^2 - ac = 0$
- 椭圆型：$b^2 - ac < 0$

## 3. 分离变量法

### 3.1 基本步骤

1. 假设解的形式：$u(x,y) = X(x)Y(y)$
2. 代入 PDE，分离变量
3. 得到两个 ODE
4. 解 ODE 并利用边界条件确定常数

### 3.2 应用举例：热方程

$u_t = k u_{xx}, \quad 0 < x < L, t > 0$

边界条件：$u(0,t) = u(L,t) = 0$

初始条件：$u(x,0) = f(x)$

解：$u(x,t) = \sum_{n=1}^{\infty} B_n \sin(\frac{n\pi x}{L}) e^{-k(\frac{n\pi}{L})^2t}$

其中 $B_n = \frac{2}{L}\int_0^L f(x)\sin(\frac{n\pi x}{L})dx$

## 4. 特征线法

### 4.1 一阶线性 PDE

形如：$au_x + bu_y = c$

特征线方程：$\frac{dy}{dx} = \frac{b}{a}$

通解：$u = F(ax - by) + \frac{c}{a}x$，其中 $F$ 是任意函数

### 4.2 准线性一阶 PDE

形如：$a(x,y,u)u_x + b(x,y,u)u_y = c(x,y,u)$

特征方程组：

$$\frac{dx}{a} = \frac{dy}{b} = \frac{du}{c}$$

## 5. Fourier 变换法

### 5.1 Fourier 变换定义

$\hat{f}(\xi) = \int_{-\infty}^{\infty} f(x)e^{-i\xi x}dx$

### 5.2 应用步骤

1. 对 PDE 进行 Fourier 变换
2. 解转换后的 ODE
3. 进行逆 Fourier 变换

### 5.3 应用举例：热方程

$u_t = ku_{xx}, \quad -\infty < x < \infty, t > 0$

初始条件：$u(x,0) = f(x)$

解：$u(x,t) = \frac{1}{\sqrt{4\pi kt}}\int_{-\infty}^{\infty} f(\xi)e^{-\frac{(x-\xi)^2}{4kt}}d\xi$

## 6. Green 函数方法

### 6.1 Green 函数定义

对于算子 $L$，Green 函数 $G(x,\xi)$ 满足：

$LG(x,\xi) = \delta(x-\xi)$

### 6.2 解的表示

对于方程 $Lu = f$，解可表示为：

$u(x) = \int_D G(x,\xi)f(\xi)d\xi$

## 7. 常见的 PDE 及其解法

### 7.1 波动方程

$u_{tt} = c^2u_{xx}$

- 分离变量法
- D'Alembert 解：$u(x,t) = f(x+ct) + g(x-ct)$

### 7.2 Laplace 方程

$u_{xx} + u_{yy} = 0$

- 分离变量法
- Green 函数法

### 7.3 扩散方程 (热方程)

$u_t = ku_{xx}$

- 分离变量法
- Fourier 变换法

## 8. 非线性 PDE 简介

### 8.1 Burgers 方程

$u_t + uu_x = \nu u_{xx}$

- Cole-Hopf 变换

### 8.2 KdV 方程

$u_t + 6uu_x + u_{xxx} = 0$

- 行波解

## 重点难点提示

- 熟练掌握 PDE 的分类方法，理解不同类型 PDE 的特点
- 重点掌握分离变量法，能够应用于波动方程、热方程和 Laplace 方程
- 理解特征线方法，尤其是在求解一阶 PDE 中的应用
- 了解 Fourier 变换在求解 PDE 中的应用，特别是无界域问题
- 掌握 Green 函数的概念和基本应用
- 对于每种常见的 PDE，要熟悉其标准形式和典型解法
- 了解一些简单的非线性 PDE 及其基本性质
