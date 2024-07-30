# 拉普拉斯变换 Laplace Transform

## 定义 Definitions

### 拉普拉斯变换 Laplace Transform

给定一个函数 $f(t)$，其拉普拉斯变换定义为

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t)e^{-st} \mathrm{d}t
$$

其中 $s$ 是复数变量。

Given a function $f(t)$, its Laplace transform is defined as

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t)e^{-st} \mathrm{d}t
$$

where $s$ is a complex variable.

### 拉普拉斯逆变换 Inverse Laplace Transform

已知 $F(s)$ 是 $f(t)$ 的拉普拉斯变换，则 $f(t)$ 的拉普拉斯逆变换定义为

$$
\mathcal{L}^{-1}\{F(s)\} = f(t) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} F(s) e^{st} \mathrm{d}s
$$

其中 $\gamma$ 是使得积分路径位于 $F(s)$ 的奇点右侧的实数。

Given $F(s)$ as the Laplace transform of $f(t)$, the inverse Laplace transform is defined as

$$
\mathcal{L}^{-1}\{F(s)\} = f(t) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} F(s) e^{st} \mathrm{d}s
$$

where $\gamma$ is a real number such that the path of integration is to the right of all singularities of $F(s)$.

## 性质 Properties

### 线性 Linearity

拉普拉斯变换是线性的，即

$$
\mathcal{L}\{a f(t) + b g(t)\} = a \mathcal{L}\{f(t)\} + b \mathcal{L}\{g(t)\}
$$

The Laplace transform is linear, i.e.,

$$
\mathcal{L}\{a f(t) + b g(t)\} = a \mathcal{L}\{f(t)\} + b \mathcal{L}\{g(t)\}
$$

### 平移定理 Shift Theorem

如果 $f(t)$ 的拉普拉斯变换是 $F(s)$，则

$$
\mathcal{L}\{e^{at} f(t)\} = F(s - a)
$$

If the Laplace transform of $f(t)$ is $F(s)$, then

$$
\mathcal{L}\{e^{at} f(t)\} = F(s - a)
$$

### 导数 Derivative

如果 $f(t)$ 的拉普拉斯变换是 $F(s)$，则

$$
\mathcal{L}\{f'(t)\} = s F(s) - f(0)
$$

If the Laplace transform of $f(t)$ is $F(s)$, then

$$
\mathcal{L}\{f'(t)\} = s F(s) - f(0)
$$

## 证明 Proof

### 拉普拉斯变换的导数性质 Proof of Derivative Property of Laplace Transform

$$
\begin{aligned}
\mathcal{L}\{f'(t)\} &= \int_0^\infty f'(t) e^{-st} \mathrm{d}t \\
&= \left[ f(t) e^{-st} \right]_0^\infty + s \int_0^\infty f(t) e^{-st} \mathrm{d}t \\
&= -f(0) + s F(s)
\end{aligned}
$$

## 利用拉普拉斯变换解微分方程 Solving Differential Equations Using Laplace Transform

### 例子 Example: 热方程 Heat Equation

考虑如下热方程 Consider the heat equation:

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

其中 $\alpha$ 是热扩散系数 where $\alpha$ is the thermal diffusivity.

**初始条件 Initial Condition**:

$$
u(x, 0) = f(x)
$$

**边界条件 Boundary Conditions**:

$$
u(0, t) = 0, \quad u(L, t) = 0
$$

1. **对时间变量 $t$ 进行拉普拉斯变换 Taking the Laplace transform with respect to $t$**:

   $$
   \mathcal{L}\left\{\frac{\partial u}{\partial t}\right\} = \alpha \mathcal{L}\left\{\frac{\partial^2 u}{\partial x^2}\right\}


$$
   记 $U(x, s) = \mathcal{L}\{u(x, t)\}$，利用拉普拉斯变换的导数性质得到：
   Let $U(x, s) = \mathcal{L}\{u(x, t)\}$, using the derivative property of the Laplace transform:
   
$$

   sU(x, s) - u(x, 0) = \alpha \frac{\partial^2 U}{\partial x^2}

$$
   代入初始条件 Substituting the initial condition $u(x, 0) = f(x)$:
   
$$

   sU(x, s) - f(x) = \alpha \frac{\partial^2 U}{\partial x^2}

$$
2. **求解常微分方程 Solving the ordinary differential equation**:
   
$$

   \frac{\partial^2 U}{\partial x^2} - \frac{s}{\alpha} U = -\frac{f(x)}{\alpha}

$$
   这是一个非齐次常系数二阶微分方程 This is a non-homogeneous second-order differential equation with constant coefficients. 
   
   其解为 The solution is:
   
$$

   U(x, s) = A(s) \sinh\left(\sqrt{\frac{s}{\alpha}} x\right) + B(s) \cosh\left(\sqrt{\frac{s}{\alpha}} x\right) + \frac{f(x)}{s}

$$
3. **应用边界条件 Applying boundary conditions**:
   
$$

   \begin{cases}

   U(0, s) = 0 \\

   U(L, s) = 0

   \end{cases}

$$
   可以求得 $A(s)$ 和 $B(s)$ We can solve for $A(s)$ and $B(s)$:
   
$$

   \begin{cases}

   B(s) = 0 \\

   A(s) \sinh\left(\sqrt{\frac{s}{\alpha}} L\right) = -\frac{f(x)}{s}

   \end{cases}

$$
   因此 Therefore:
   
$$

   U(x, s) = -\frac{f(x)}{s} \frac{\sinh\left(\sqrt{\frac{s}{\alpha}} x\right)}{\sinh\left(\sqrt{\frac{s}{\alpha}} L\right)}

$$
4. **进行拉普拉斯逆变换 Taking the inverse Laplace transform**:
   
$$

   u(x, t) = \mathcal{L}^{-1}\left\{ U(x, s) \right\}

$$
   利用拉普拉斯逆变换，我们可以得到 $u(x, t)$ 的表达式 Using the inverse Laplace transform, we can obtain the expression for $u(x, t)$.

通过拉普拉斯变换和逆变换，我们可以解决一类偏微分方程 This demonstrates the method of solving a class of partial differential equations using Laplace transform and its inverse.
