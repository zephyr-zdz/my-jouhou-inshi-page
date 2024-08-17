# Inequality for Integrals | 积分不等式

## 1. Jensen's Inequality | 詹森不等式

### Definition | 定义

Jensen's inequality applies to a convex function $f$ and a random variable $X$. It states that for any convex function $f$ and integrable random variable $X$:

$$
f\left(\mathbb{E}[X]\right) \leq \mathbb{E}[f(X)]
$$

若 $f$ 是凸函数且 $X$ 是可积随机变量，则詹森不等式表明：

$$
f\left(\mathbb{E}[X]\right) \leq \mathbb{E}[f(X)]
$$

### Usage | 使用

- **Convex Functions**: Ensure $f$ is convex, which means $f''(x) \geq 0$ for all $x$.
- **Expectation of a Random Variable**: Useful in probability theory, particularly when working with expectations.

- **凸函数**：确保 $f$ 是凸函数，即 $f''(x) \geq 0$ 对所有 $x$ 成立
- **随机变量的期望**：在概率论中非常有用，特别是在处理期望时

### Proof | 证明

1. By definition, a function $f$ is convex if for any $x_1, x_2 \in \mathbb{R}$ and $\lambda \in [0, 1]$:

$$
f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) + (1-\lambda)f(x_2)
$$

根据定义，若函数 $f$ 是凸函数，则对于任意的 $x_1, x_2 \in \mathbb{R}$ 和 $\lambda \in [0, 1]$，有：

$$
f(\lambda x_1 + (1-\lambda)x_2) \leq \lambda f(x_1) + (1-\lambda)f(x_2)
$$

2. Take the expectation over the inequality where $X$ is a random variable, using $\lambda = \frac{1}{n}$ for discrete cases or integral form for continuous cases.

对该不等式取期望，其中 $X$ 是随机变量，在离散情形下使用 $\lambda = \frac{1}{n}$，在连续情形下使用积分形式

3. The inequality leads to:

$$
f\left(\mathbb{E}[X]\right) \leq \mathbb{E}[f(X)]
$$

该不等式导出：

$$
f\left(\mathbb{E}[X]\right) \leq \mathbb{E}[f(X)]
$$

## 2. Hölder's Inequality | Hölder 不等式

### Definition | 定义

Hölder's inequality provides a bound on the integral (or sum) of the product of functions. If $p > 1$ and $q > 1$ satisfy $\frac{1}{p} + \frac{1}{q} = 1$, then for integrable functions $f$ and $g$:

$$
\int |f(x)g(x)| \, \mathrm{d}x \leq \left( \int |f(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} \left( \int |g(x)|^q \, \mathrm{d}x \right)^{\frac{1}{q}}
$$

Hölder 不等式为函数积的积分（或和）提供了一个界。若 $p > 1$ 且 $q > 1$ 满足 $\frac{1}{p} + \frac{1}{q} = 1$，则对可积函数 $f$ 和 $g$，有：

$$
\int |f(x)g(x)| \, \mathrm{d}x \leq \left( \int |f(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} \left( \int |g(x)|^q \, \mathrm{d}x \right)^{\frac{1}{q}}
$$

### Usage | 使用

- **Normed Spaces**: Essential in proving the Minkowski inequality and establishing norms.
- **L^p Spaces**: Often used in functional analysis, particularly in $L^p$ spaces.

- **赋范空间**：在证明 Minkowski 不等式和建立范数时至关重要
- **$L^p$ 空间**：在泛函分析中经常使用，特别是在 $L^p$ 空间中

### Proof | 证明

1. Start with the convexity of the exponential function, which is a special case of Young's inequality:

$$
ab \leq \frac{a^p}{p} + \frac{b^q}{q} \quad \text{where} \quad \frac{1}{p} + \frac{1}{q} = 1
$$

从指数函数的凸性开始，这是 Young 不等式的特例：

$$
ab \leq \frac{a^p}{p} + \frac{b^q}{q} \quad \text{其中} \quad \frac{1}{p} + \frac{1}{q} = 1
$$

2. Integrate both sides:

$$
\int |f(x)g(x)| \, \mathrm{d}x \leq \int \left( \frac{|f(x)|^p}{p} + \frac{|g(x)|^q}{q} \right) \, \mathrm{d}x
$$

对双方积分：

$$
\int |f(x)g(x)| \, \mathrm{d}x \leq \int \left( \frac{|f(x)|^p}{p} + \frac{|g(x)|^q}{q} \right) \, \mathrm{d}x
$$

3. Apply the definition of $L^p$ and $L^q$ norms to complete the proof.

应用 $L^p$ 和 $L^q$ 范数的定义完成证明

## 3. Minkowski's Inequality | Minkowski 不等式

### Definition | 定义

Minkowski's inequality is a generalization of the triangle inequality to integrals. For integrable functions $f$ and $g$, and $p \geq 1$:

$$
\left( \int |f(x) + g(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} \leq \left( \int |f(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} + \left( \int |g(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}}
$$

Minkowski 不等式是三角不等式对积分的推广。对可积函数 $f$ 和 $g$，以及 $p \geq 1$：

$$
\left( \int |f(x) + g(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} \leq \left( \int |f(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} + \left( \int |g(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}}
$$

### Usage | 使用

- **$L^p$ Spaces**: Fundamental in the study of $L^p$ spaces, particularly in proving that these spaces are normed vector spaces.
- **Distance Measurement**: Used in defining the distance between functions in $L^p$ spaces.

- **$L^p$ 空间**：在 $L^p$ 空间研究中具有基础性意义，特别是在证明这些空间是赋范向量空间时
- **距离度量**：用于定义 $L^p$ 空间中函数之间的距离

### Proof | 证明

1. Apply Hölder's inequality to the sum of $f$ and $g$ raised to the power $p$.

对 $f$ 和 $g$ 的和取 $p$ 次方后，应用 Hölder 不等式

2. The result follows by combining terms and recognizing the definition of the $L^p$ norm.

通过合并项并识别 $L^p$ 范数的定义，得出结果

$$
\left( \int |f(x) + g(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} \leq \left( \int |f(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}} + \left( \int |g(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}}
$$

## 4. Cauchy-Schwarz Inequality | 柯西-施瓦茨不等式

### Definition | 定义

The Cauchy-Schwarz inequality is a fundamental result in linear algebra and analysis. It states that for any two integrable functions $f$ and $g$ on a measurable space, the following inequality holds:

$$
\left( \int |f(x)g(x)| \, \mathrm{d}x \right)^2 \leq \left( \int |f(x)|^2 \, \mathrm{d}x \right) \left( \int |g(x)|^2 \, \mathrm{d}x \right)
$$

柯西-施瓦茨不等式是线性代数和分析中的一个基本结果。它表明，对于测度空间上的任意两个可积函数 $f$ 和 $g$，有如下不等式成立：

$$
\left( \int |f(x)g(x)| \, \mathrm{d}x \right)^2 \leq \left( \int |f(x)|^2 \, \mathrm{d}x \right) \left( \int |g(x)|^2 \, \mathrm{d}x \right)
$$

### Parametric Form | 参数形式

For real numbers $a$, $b$, and a parameter $t \in [0,1]$, the Cauchy-Schwarz inequality can be expressed as:

$$
((1-t)a + tb)^2 \leq (1-t)a^2 + tb^2
$$

对于实数 $a$、$b$ 和参数 $t \in [0,1]$，柯西-施瓦茨不等式可以表示为：

$$
((1-t)a + tb)^2 \leq (1-t)a^2 + tb^2
$$

### Usage | 使用

- **Inner Product Spaces**: Provides a bound on the inner product, critical in defining angles and orthogonality.
- **Distance Measurement**: Used to establish the triangle inequality in normed vector spaces.
- **Convexity Proofs**: The parametric form is often used in proving the convexity of functionals in variational problems.

- **内积空间**：为内积提供了一个上界，对定义角度和正交性至关重要。
- **距离度量**：用于在赋范向量空间中确立三角不等式。
- **凸性证明**：参数形式常用于证明变分问题中泛函的凸性。

### Proof | 证明

1. Consider the integral of the square of the linear combination $f(x) + \lambda g(x)$ for a scalar $\lambda$:

   $$
   \int |f(x) + \lambda g(x)|^2 \, \mathrm{d}x \geq 0
   $$

   考虑 $f(x) + \lambda g(x)$ 的线性组合的平方积分，其中 $\lambda$ 为标量：

   $$
   \int |f(x) + \lambda g(x)|^2 \, \mathrm{d}x \geq 0
   $$

2. Expand the square and integrate each term:

   $$
   \int |f(x)|^2 \, \mathrm{d}x + 2\lambda \int f(x)g(x) \, \mathrm{d}x + \lambda^2 \int |g(x)|^2 \, \mathrm{d}x \geq 0
   $$

   展开平方并对每一项积分：

   $$
   \int |f(x)|^2 \, \mathrm{d}x + 2\lambda \int f(x)g(x) \, \mathrm{d}x + \lambda^2 \int |g(x)|^2 \, \mathrm{d}x \geq 0
   $$

3. The quadratic form in $\lambda$ must be non-negative for all $\lambda$, leading to the discriminant condition:

   $$
   \left( \int f(x)g(x) \, \mathrm{d}x \right)^2 \leq \left( \int |f(x)|^2 \, \mathrm{d}x \right) \left( \int |g(x)|^2 \, \mathrm{d}x \right)
   $$

   对于所有 $\lambda$，该二次型必须非负，从而得到判别式条件：

   $$
   \left( \int f(x)g(x) \, \mathrm{d}x \right)^2 \leq \left( \int |f(x)|^2 \, \mathrm{d}x \right) \left( \int |g(x)|^2 \, \mathrm{d}x \right)
   $$

4. This completes the proof of the Cauchy-Schwarz inequality.

   由此完成柯西-施瓦茨不等式的证明。

### Proof of Parametric Form | 参数形式的证明

1. Expand the left side of the inequality:

   $$
   ((1-t)a + tb)^2 = (1-t)^2a^2 + 2t(1-t)ab + t^2b^2
   $$

   展开不等式的左边：

   $$
   ((1-t)a + tb)^2 = (1-t)^2a^2 + 2t(1-t)ab + t^2b^2
   $$

2. Subtract the right side:

   $$
   \begin{align*}
   &((1-t)a + tb)^2 - ((1-t)a^2 + tb^2) \\
   &= (1-t)^2a^2 + 2t(1-t)ab + t^2b^2 - (1-t)a^2 - tb^2 \\
   &= ((1-t)^2 - (1-t))a^2 + 2t(1-t)ab + (t^2 - t)b^2
   \end{align*}
   $$

   减去右边：

   $$
   \begin{align*}
   &((1-t)a + tb)^2 - ((1-t)a^2 + tb^2) \\
   &= (1-t)^2a^2 + 2t(1-t)ab + t^2b^2 - (1-t)a^2 - tb^2 \\
   &= ((1-t)^2 - (1-t))a^2 + 2t(1-t)ab + (t^2 - t)b^2
   \end{align*}
   $$

3. Factor out $-t(1-t)$:

   $$
   \begin{align*}
   &= -t(1-t)a^2 + 2t(1-t)ab - t(1-t)b^2 \\
   &= -t(1-t)(a^2 - 2ab + b^2) \\
   &= -t(1-t)(a-b)^2
   \end{align*}
   $$

   提取公因子 $-t(1-t)$：

   $$
   \begin{align*}
   &= -t(1-t)a^2 + 2t(1-t)ab - t(1-t)b^2 \\
   &= -t(1-t)(a^2 - 2ab + b^2) \\
   &= -t(1-t)(a-b)^2
   \end{align*}
   $$

4. Since $t \in [0,1]$, we know that $t(1-t) \geq 0$. Therefore:

   $$
   -t(1-t)(a-b)^2 \leq 0
   $$

   由于 $t \in [0,1]$，我们知道 $t(1-t) \geq 0$。因此：

   $$
   -t(1-t)(a-b)^2 \leq 0
   $$

This proves the parametric form of the Cauchy-Schwarz inequality.

这就证明了柯西-施瓦茨不等式的参数形式。
