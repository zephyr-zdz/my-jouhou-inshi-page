# Residue Theory and Its Applications

# 留数理论及其应用

## 1. Introduction 简介

Residue theory is a powerful tool in complex analysis for evaluating certain integrals and series.

留数理论是复分析中用于计算某些积分和级数的强大工具。

## 2. Key Concepts 核心概念

### 2.1 Residue 留数

**Definition 定义**:
The residue of a meromorphic function $f(z)$ at a singularity $a$ is the coefficient of $(z-a)^{-1}$ in the Laurent series expansion of $f(z)$ about $a$.
函数 $f(z)$ 在奇点 $a$ 处的留数是 $f(z)$ 在 $a$ 处的洛朗级数展开中 $(z-a)^{-1}$ 项的系数。

**Notation 记号**: $\text{Res}(f,a)$ or $\text{Res}_{z=a}f(z)$

### 2.2 Types of Singularities 奇点类型

1. **Removable Singularity 可去奇点**:
   - $\lim_{z \to a}(z-a)f(z) = 0$
   - Residue is 0 留数为 0

2. **Simple Pole 简单极点**:
   - $\lim_{z \to a}(z-a)f(z)$ exists and is non-zero
   - $\lim_{z \to a}(z-a)f(z)$ 存在且不为零

3. **Pole of Order m m 阶极点**:
   - $\lim_{z \to a}(z-a)^mf(z)$ exists and is non-zero
   - $\lim_{z \to a}(z-a)^mf(z)$ 存在且不为零

4. **Essential Singularity 本性奇点**:
   - Neither removable nor a pole
   - 既不是可去奇点也不是极点

## 3. Residue Calculation Techniques 留数计算技巧

### 3.1 For Simple Poles 简单极点

$$
\text{Res}(f,a) = \lim_{z \to a}(z-a)f(z)
$$

### 3.2 For Poles of Order m m 阶极点

$$
\text{Res}(f,a) = \frac{1}{(m-1)!}\lim_{z \to a}\frac{d^{m-1}}{dz^{m-1}}[(z-a)^mf(z)]
$$

### 3.3 Using Laurent Series 使用洛朗级数

If $f(z) = \sum_{n=-\infty}^{\infty}a_n(z-a)^n$, then:

如果 $f(z) = \sum_{n=-\infty}^{\infty}a_n(z-a)^n$，那么：

$$
\text{Res}(f,a) = a_{-1}
$$

## 4. Residue Theorem 留数定理

**Statement 陈述**:
Let $f(z)$ be meromorphic in a simply connected domain $D$, and let $C$ be a simple closed contour in $D$. If $f(z)$ has finitely many singularities $a_1, a_2, …, a_n$ inside $C$, then:
设 $f(z)$ 在单连通区域 $D$ 内亚纯，$C$ 是 $D$ 内的简单闭合曲线。如果 $f(z)$ 在 $C$ 内有有限个奇点 $a_1, a_2, …, a_n$，则：

$$
\oint_C f(z)dz = 2\pi i \sum_{k=1}^n \text{Res}(f,a_k)
$$

## 5. Applications 应用

### 5.1 Evaluation of Real Integrals 实积分的计算

For $\int_{-\infty}^{\infty}f(x)dx$, consider $\oint_C f(z)dz$ where $C$ is a semicircle in the upper half-plane.

对于 $\int_{-\infty}^{\infty}f(x)dx$，考虑 $\oint_C f(z)dz$，其中 $C$ 是上半平面的半圆。

### 5.2 Summation of Series 级数求和

For $\sum_{n=-\infty}^{\infty}f(n)$, consider $\frac{\pi}{\sin(\pi z)}f(z)$ and its residues.

对于 $\sum_{n=-\infty}^{\infty}f(n)$，考虑 $\frac{\pi}{\sin(\pi z)}f(z)$ 及其留数。

### 5.3 Argument Principle 辐角原理

$$
N - P = \frac{1}{2\pi i}\oint_C \frac{f'(z)}{f(z)}dz
$$

Where $N$ is the number of zeros and $P$ is the number of poles of $f(z)$ inside $C$, counting multiplicity.

其中 $N$ 是 $f(z)$ 在 $C$ 内的零点数，$P$ 是极点数，计算重数。

## 6. Common Mistakes to Avoid 常见错误

1. Forgetting to check if all singularities are inside the contour.
   忘记检查是否所有奇点都在轮廓内。

2. Misidentifying the order of a pole.
   错误识别极点的阶数。

3. Neglecting to consider residues at infinity for improper integrals.
   对于非正常积分，忽略了无穷远处的留数。

4. Incorrectly applying the residue theorem to non-meromorphic functions.
   错误地将留数定理应用于非亚纯函数。

## 7. Practice Problems 练习题

1. Calculate $\int_{0}^{\infty}\frac{dx}{1+x^4}$ using residue theory.
   使用留数理论计算 $\int_{0}^{\infty}\frac{dx}{1+x^4}$。

2. Find the sum of the series $\sum_{n=1}^{\infty}\frac{1}{n^2}$ using residue theory.
   使用留数理论求级数 $\sum_{n=1}^{\infty}\frac{1}{n^2}$ 的和。

3. Evaluate $\oint_{|z|=2}\frac{e^z}{z^3(z-1)}dz$.
   计算 $\oint_{|z|=2}\frac{e^z}{z^3(z-1)}dz$。
