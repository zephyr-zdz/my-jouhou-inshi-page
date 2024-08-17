# Definite Integrals / 定积分

## Introduction / 介绍

Definite integrals are used to calculate the area under a curve over a specific interval. This cheat sheet summarizes key definitions, properties, and techniques for evaluating definite integrals, including those with infinite limits.

定积分用于计算在特定区间下曲线的面积。此备忘单总结了定积分的关键定义、性质和计算技巧，包括无穷界限的积分。

## Definitions / 定义

### Definite Integral / 定积分

The definite integral of a function $f(x)$ from $a$ to $b$ is denoted by:

函数 $f(x)$ 从 $a$ 到 $b$ 的定积分表示为：

$$
 \int_{a}^{b} f(x) \, dx 
$$

### Fundamental Theorem of Calculus / 微积分基本定理

If $F(x)$ is an antiderivative of $f(x)$, then:

如果 $F(x)$ 是 $f(x)$ 的一个原函数，则：

$$
 \int_{a}^{b} f(x) \, dx = F(b) - F(a) 
$$

## Properties / 性质

1. **Linearity / 线性性质**

   $$
   \int_{a}^{b} [cf(x) + g(x)] \, dx = c\int_{a}^{b} f(x) \, dx + \int_{a}^{b} g(x) \, dx


$$

   where $c$ is a constant. / 其中 $c$ 是常数。

2. **Additivity on Intervals / 区间可加性**
   $$

   \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx = \int_{a}^{b} f(x) \, dx

$$

3. **Reversal of Limits / 上下限互换**
   $$

   \int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx

$$

4. **Zero Width Interval / 零宽度区间**
   $$

   \int_{a}^{a} f(x) \, dx = 0

$$

## Techniques for Evaluation / 计算技巧

### Basic Techniques / 基本技巧

1. **Substitution Method / 代换法**
   Change of variable: / 变量替换：
   $$

   \int_{a}^{b} f(g(x))g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du

$$

2. **Integration by Parts / 分部积分法**
   $$

   \int_{a}^{b} u(x)v'(x) \, dx = \left[ u(x)v(x) \right]_{a}^{b} - \int_{a}^{b} u'(x)v(x) \, dx

$$
   where $u(x)$ and $v(x)$ are continuously differentiable functions on $[a, b]$. / 其中 $u(x)$ 和 $v(x)$ 在 $[a, b]$ 上是连续可微函数。

### Special Techniques / 特殊技巧

1. **Improper Integrals / 广义积分**

   When the upper or lower limit (or both) is infinite, or the integrand becomes infinite within the interval of integration.

   当积分的上限或下限（或两者）是无穷大，或者被积函数在积分区间内变为无穷大时。

   $$

   \int_{a}^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_{a}^{b} f(x) \, dx

$$

   $$

   \int_{-\infty}^{b} f(x) \, dx = \lim_{a \to -\infty} \int_{a}^{b} f(x) \, dx

$$

   $$

   \int_{-\infty}^{\infty} f(x) \, dx = \lim_{a \to -\infty, b \to \infty} \int_{a}^{b} f(x) \, dx

$$

## Examples / 示例

### Basic Example / 基本示例

Evaluate $\int_{0}^{2} (3x^2 + 2x + 1) \, dx$:

计算 $\int_{0}^{2} (3x^2 + 2x + 1) \, dx$：

$$

\begin{align*}

\int_{0}^{2} (3x^2 + 2x + 1) \, dx &= \left[ x^3 + x^2 + x \right]_{0}^{2} \\

&= (2^3 + 2^2 + 2) - (0^3 + 0^2 + 0) \\

&= 8 + 4 + 2 \\

&= 14

\end{align*}

$$

### Improper Integral Example / 广义积分示例

Evaluate $\int_{1}^{\infty} \frac{1}{x^2} \, dx$:

计算 $\int_{1}^{\infty} \frac{1}{x^2} \, dx$：

$$

\begin{align*}

\int_{1}^{\infty} \frac{1}{x^2} \, dx &= \lim_{b \to \infty} \int_{1}^{b} \frac{1}{x^2} \, dx \\

&= \lim_{b \to \infty} \left[ -\frac{1}{x} \right]_{1}^{b} \\

&= \lim_{b \to \infty} \left( -\frac{1}{b} + \frac{1}{1} \right) \\

&= 0 + 1 \\

&= 1

\end{align*}

$$

## Common Integrals / 常见积分

1. $\int_{a}^{b} k \, dx = k(b - a)$

2. $\int_{a}^{b} x \, dx = \frac{1}{2} (b^2 - a^2)$

3. $\int_{a}^{b} x^2 \, dx = \frac{1}{3} (b^3 - a^3)$

4. $\int_{a}^{b} e^x \, dx = e^x \Big|_{a}^{b} = e^b - e^a$

5. $\int_{a}^{b} \sin(x) \, dx = -\cos(x) \Big|_{a}^{b} = -\cos(b) + \cos(a)$

6. $\int_{a}^{b} \cos(x) \, dx = \sin(x) \Big|_{a}^{b} = \sin(b) - \sin(a)$


---
## Advanced Calculation Techniques / 进阶计算技巧

### 1. Exchange of Limits and Integration / 积分与极限的交换

#### Concept / 概念
In some cases, it is possible to exchange the order of a limit and an integral. This is often used in more advanced calculus, particularly in series and sequences of functions.

在某些情况下，可以交换极限和积分的顺序。这在更高阶的微积分中尤为常见，特别是在函数的级数和序列中。

#### Theorem / 定理
If $f(x, t)$ is a function such that the following conditions are satisfied:
- $f(x, t)$ is continuous in $x$ for each fixed $t$,
- The limit $\lim_{t \to t_0} f(x, t)$ exists for each $x$ in the interval $[a, b]$,
- There exists an integrable function $g(x)$ such that $|f(x, t)| \leq g(x)$ for all $t$ near $t_0$,

then:
$$

\lim_{t \to t_0} \int_{a}^{b} f(x, t) \, dx = \int_{a}^{b} \lim_{t \to t_0} f(x, t) \, dx

$$

如果函数 $f(x, t)$ 满足以下条件：
- 对于每一个固定的 $t$， $f(x, t)$ 在 $x$ 上是连续的，
- 对于区间 $[a, b]$ 上的每个 $x$，极限 $\lim_{t \to t_0} f(x, t)$ 存在，
- 存在一个可积函数 $g(x)$，使得对于所有 $t$ 近 $t_0$ 时 $|f(x, t)| \leq g(x)$，

则有：
$$

\lim_{t \to t_0} \int_{a}^{b} f(x, t) \, dx = \int_{a}^{b} \lim_{t \to t_0} f(x, t) \, dx

$$

#### Example / 示例
Evaluate $\lim_{n \to \infty} \int_{0}^{1} x^n \, dx$:

计算 $\lim_{n \to \infty} \int_{0}^{1} x^n \, dx$：

$$

\begin{align*}

\int_{0}^{1} x^n \, dx &= \left[ \frac{x^{n+1}}{n+1} \right]_{0}^{1} \\

&= \frac{1}{n+1}

\end{align*}

$$

$$

\lim_{n \to \infty} \int_{0}^{1} x^n \, dx = \lim_{n \to \infty} \frac{1}{n+1} = 0

$$

### 2. Differentiation Under the Integral Sign / 积分号下微分

#### Concept / 概念
This technique allows differentiation of an integral with respect to a parameter.

这一技巧允许我们对含参数积分的参数进行微分。

#### Theorem (Leibniz Integral Rule) / 定理（莱布尼兹积分法则）
If $f(x, t)$ is continuous on $[a, b] \times [c, d]$ and has a continuous partial derivative with respect to $t$, then:

如果函数 $f(x, t)$ 在 $[a, b] \times [c, d]$ 上连续，并且它对 $t$ 的偏导数也是连续的，那么：

$$

\frac{d}{dt} \int_{a(t)}^{b(t)} f(x, t) \, dx = f(b(t), t) \frac{db(t)}{dt} - f(a(t), t) \frac{da(t)}{dt} + \int_{a(t)}^{b(t)} \frac{\partial}{\partial t} f(x, t) \, dx

$$

#### Example / 示例
Evaluate $\frac{d}{dt} \int_{0}^{t} e^{-x^2} \, dx$:

计算 $\frac{d}{dt} \int_{0}^{t} e^{-x^2} \, dx$：

$$

\begin{align*}

\frac{d}{dt} \int_{0}^{t} e^{-x^2} \, dx &= e^{-t^2} \cdot \frac{d}{dt}(t) - e^{-0^2} \cdot \frac{d}{dt}(0) + \int_{0}^{t} \frac{\partial}{\partial t} (e^{-x^2}) \, dx \\

&= e^{-t^2}

\end{align*}

$$

### 3. Fubini's Theorem / 富比尼定理

#### Concept / 概念
Fubini's theorem provides conditions under which a double integral can be computed as an iterated integral.

富比尼定理提供了双重积分可以作为迭代积分计算的条件。

#### Theorem / 定理
If $f(x, y)$ is continuous on the rectangle $[a, b] \times [c, d]$, then:

如果函数 $f(x, y)$ 在矩形 $[a, b] \times [c, d]$ 上是连续的，那么：

$$

\int_{a}^{b} \int_{c}^{d} f(x, y) \, dy \, dx = \int_{c}^{d} \int_{a}^{b} f(x, y) \, dx \, dy

$$

#### Example / 示例
Evaluate $\int_{0}^{1} \int_{0}^{1} xy \, dx \, dy$:

计算 $\int_{0}^{1} \int_{0}^{1} xy \, dx \, dy$：

$$

\begin{align*}

\int_{0}^{1} \int_{0}^{1} xy \, dx \, dy &= \int_{0}^{1} \left( \int_{0}^{1} xy \, dx \right) dy \\

&= \int_{0}^{1} \left( y \int_{0}^{1} x \, dx \right) dy \\

&= \int_{0}^{1} \left( y \cdot \frac{1}{2} \right) dy \\

&= \frac{1}{2} \int_{0}^{1} y \, dy \\

&= \frac{1}{2} \cdot \frac{1}{2} \\

&= \frac{1}{4}

\end{align*}

$$

These advanced techniques are powerful tools for evaluating complex integrals and are widely used in both theoretical and applied mathematics.

这些进阶技巧是计算复杂积分的有力工具，广泛应用于理论和应用数学中。

---
