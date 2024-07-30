# Orthogonality of Sine Functions

## Orthogonality of Sine Functions / 正弦函数的正交性

The orthogonality property of sine functions over the interval $[0, 1]$ states that:

正弦函数在区间 $[0, 1]$ 上的正交性质如下：

$$
\int_0^1 \sin(n\pi x) \sin(m\pi x) \, \mathrm{d}x = 0 \quad \text{if} \quad n \neq m,
$$

and / 且

$$
\int_0^1 \sin(n\pi x) \sin(m\pi x) \, \mathrm{d}x = \frac{1}{2} \quad \text{if} \quad n = m.
$$

### Proof of Orthogonality / 正交性的证明

To prove this property, we can use trigonometric identities and properties of integrals.

为了证明这个性质，我们可以使用三角恒等式和积分性质。

First, consider the product-to-sum identities for sine functions:

首先，考虑正弦函数的积化和公式：

$$
\sin(n\pi x) \sin(m\pi x) = \frac{1}{2} \left[\cos((n-m)\pi x) - \cos((n+m)\pi x)\right].
$$

Using this identity, the integral becomes:

利用这个公式，积分变为：

$$
\int_0^1 \sin(n\pi x) \sin(m\pi x) \, \mathrm{d}x = \frac{1}{2} \int_0^1 \left[\cos((n-m)\pi x) - \cos((n+m)\pi x)\right] \, \mathrm{d}x.
$$

Now, we evaluate the two integrals separately.

现在，我们分别计算这两个积分。

1. Integral of $\cos((n-m)\pi x)$:


   $\cos((n-m)\pi x)$ 的积分：

   $$
   \int_0^1 \cos((n-m)\pi x) \, \mathrm{d}x.

$$

   When $n \neq m$:
   
   当 $n \neq m$ 时：

   $$

   \int_0^1 \cos((n-m)\pi x) \, \mathrm{d}x = \left[ \frac{\sin((n-m)\pi x)}{(n-m)\pi} \right]_0^1 = \frac{\sin((n-m)\pi)}{(n-m)\pi} - \frac{\sin(0)}{(n-m)\pi} = 0.

$$

   When $n = m$:
   
   当 $n = m$ 时：

   $$

   \int_0^1 \cos((n-m)\pi x) \, \mathrm{d}x = \int_0^1 \cos(0) \, \mathrm{d}x = \int_0^1 1 \, \mathrm{d}x = 1.

$$

2. Integral of $\cos((n+m)\pi x)$:
   
   $\cos((n+m)\pi x)$ 的积分：

   $$

   \int_0^1 \cos((n+m)\pi x) \, \mathrm{d}x.

$$

   For any positive integers $n$ and $m$:
   
   对于任意正整数 $n$ 和 $m$：

   $$

   \int_0^1 \cos((n+m)\pi x) \, \mathrm{d}x = \left[ \frac{\sin((n+m)\pi x)}{(n+m)\pi} \right]_0^1 = \frac{\sin((n+m)\pi)}{(n+m)\pi} - \frac{\sin(0)}{(n+m)\pi} = 0.

$$

Combining these results, we have:

结合这些结果，我们得到：

- When $n \neq m$:
  
  当 $n \neq m$ 时：

  $$

  \int_0^1 \sin(n\pi x) \sin(m\pi x) \, \mathrm{d}x = \frac{1}{2} \left(0 - 0\right) = 0.

$$

- When $n = m$:
  
  当 $n = m$ 时：

  $$

  \int_0^1 \sin(n\pi x) \sin(n\pi x) \, \mathrm{d}x = \frac{1}{2} \left(1 - 0\right) = \frac{1}{2}.

$$

Therefore, the orthogonality property of sine functions is verified:
  
因此，正弦函数的正交性得以验证：

$$

\int_0^1 \sin(n\pi x) \sin(m\pi x) \, \mathrm{d}x = \begin{cases}

0 & \text{if } n \neq m, \\

\frac{1}{2} & \text{if } n = m.

\end{cases}

$$

This property simplifies many problems involving Fourier series and orthogonal functions, as it allows us to separate coefficients in series expansions cleanly.

这个性质简化了许多涉及傅里叶级数和正交函数的问题，因为它使我们能够清晰地分离级数展开中的系数。

### Other Orthogonality Properties of Functions / 其他函数的正交性性质

In addition to sine functions, other families of functions also exhibit orthogonality properties. Two common examples are the cosine functions and the Legendre polynomials.

除了正弦函数之外，其他函数族也具有正交性性质。两个常见的例子是余弦函数和勒让德多项式。

#### Orthogonality of Cosine Functions / 余弦函数的正交性

The orthogonality property of cosine functions over the interval $[0, 1]$ states that:

余弦函数在区间 $[0, 1]$ 上的正交性质如下：

$$

\int_0^1 \cos(n\pi x) \cos(m\pi x) \, \mathrm{d}x = 0 \quad \text{if} \quad n \neq m,

$$

and / 且

$$

\int_0^1 \cos(n\pi x) \cos(m\pi x) \, \mathrm{d}x = \frac{1}{2} \quad \text{if} \quad n = m \neq 0,

$$

$$

\int_0^1 \cos(0) \cos(0) \, \mathrm{d}x = 1.

$$

#### Orthogonality of Legendre Polynomials / 勒让德多项式的正交性

Legendre polynomials are orthogonal over the interval $[-1, 1]$ with respect to the weight function $1$. The orthogonality property is given by:

勒让德多项式在区间 $[-1, 1]$ 上关于权函数 $1$ 是正交的。正交性质如下：

$$

\int_{-1}^1 P_n(x) P_m(x) \, \mathrm{d}x = 0 \quad \text{if} \quad n \neq m,

$$

and / 且

$$

\int_{-1}^1 P_n(x) P_n(x) \, \mathrm{d}x = \frac{2}{2n + 1}.

$$

### Applications of Orthogonality / 正交性的应用

These orthogonality properties are crucial in various fields such as signal processing, quantum mechanics, and numerical analysis. They facilitate the decomposition of functions into orthogonal basis functions, simplifying calculations and improving computational efficiency.

这些正交性性质在信号处理、量子力学和数值分析等多个领域中至关重要。它们使得函数可以分解为正交基函数，简化了计算并提高了计算效率。
