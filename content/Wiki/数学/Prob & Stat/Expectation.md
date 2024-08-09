# Expectation Values｜期望值

## Definition｜定义

**Expectation** of a random variable $\mathbf{X}$, denoted by $\mathbb{E}[\mathbf{X}]$ or $E(\mathbf{X})$, is the long-run average value of repetitions of the experiment it represents. It's also known as the **mean**.  
随机变量$\mathbf{X}$的**期望**，记作$\mathbb{E}[\mathbf{X}]$或$E(\mathbf{X})$，是该实验重复多次后得到的平均值。期望也称为**均值**。

## Important Properties｜重要性质

1. **Linearity of Expectation**｜期望的线性性质:
   - $\mathbb{E}[a\mathbf{X} + b\mathbf{Y}] = a\mathbb{E}[\mathbf{X}] + b\mathbb{E}[\mathbf{Y}]$
   - This holds for any real numbers $a$ and $b$, and random variables $\mathbf{X}$ and $\mathbf{Y}$.  
     这对任意实数$a$和$b$以及随机变量$\mathbf{X}$和$\mathbf{Y}$都成立。

2. **Expectation of a Constant**｜常数的期望:
   - $\mathbb{E}[c] = c$ where $c$ is a constant.  
     如果$c$是常数，那么$\mathbb{E}[c] = c$。

3. **Non-negativity**｜非负性:
   - If $\mathbf{X} \geq 0$ almost surely, then $\mathbb{E}[\mathbf{X}] \geq 0$.  
     如果$\mathbf{X}$几乎肯定非负，那么$\mathbb{E}[\mathbf{X}] \geq 0$。

4. **Law of the Unconscious Statistician**｜无意识统计学家法则:
   - If $\mathbf{X}$ is a random variable and $g$ is a function, then $\mathbb{E}[g(\mathbf{X})]$ is not necessarily $g(\mathbb{E}[\mathbf{X}])$. However, $\mathbb{E}[g(\mathbf{X})] = \int_{-\infty}^{\infty} g(x) f_{\mathbf{X}}(x) \mathrm{d}x$, where $f_{\mathbf{X}}(x)$ is the probability density function of $\mathbf{X}$.  
     如果$\mathbf{X}$是随机变量，$g$是一个函数，那么$\mathbb{E}[g(\mathbf{X})]$不一定等于$g(\mathbb{E}[\mathbf{X}])$。然而，$\mathbb{E}[g(\mathbf{X})] = \int_{-\infty}^{\infty} g(x) f_{\mathbf{X}}(x) \mathrm{d}x$，其中$f_{\mathbf{X}}(x)$是$\mathbf{X}$的概率密度函数。

## Common Formulas｜常用公式

1. **Discrete Random Variables**｜离散随机变量:
   - For a discrete random variable $\mathbf{X}$ with possible values $x_1, x_2, \ldots$ and corresponding probabilities $p_1, p_2, \ldots$:

     $$
     \mathbb{E}[\mathbf{X}] = \sum_{i} x_i p_i
     $$

     对于一个具有可能取值$x_1, x_2, \ldots$以及相应概率$p_1, p_2, \ldots$的离散随机变量$\mathbf{X}$：

     $$
     \mathbb{E}[\mathbf{X}] = \sum_{i} x_i p_i
     $$

2. **Continuous Random Variables**｜连续随机变量:
   - For a continuous random variable $\mathbf{X}$ with probability density function $f_{\mathbf{X}}(x)$:
     $$
     \mathbb{E}[\mathbf{X}] = \int_{-\infty}^{\infty} x f_{\mathbf{X}}(x) \mathrm{d}x
     $$
     对于具有概率密度函数$f_{\mathbf{X}}(x)$的连续随机变量$\mathbf{X}$：

     $$
     \mathbb{E}[\mathbf{X}] = \int_{-\infty}^{\infty} x f_{\mathbf{X}}(x) \mathrm{d}x
     $$

3. **Expectation of the Sum**｜和的期望:
   - For any two random variables $\mathbf{X}$ and $\mathbf{Y}$:

     $$
     \mathbb{E}[\mathbf{X} + \mathbf{Y}] = \mathbb{E}[\mathbf{X}] + \mathbb{E}[\mathbf{Y}]
     $$

     对于任意两个随机变量$\mathbf{X}$和$\mathbf{Y}$：

     $$
     \mathbb{E}[\mathbf{X} + \mathbf{Y}] = \mathbb{E}[\mathbf{X}] + \mathbb{E}[\mathbf{Y}]
     $$

4. **Higher Moments**｜高阶矩:
   - The $n$-th moment of a random variable $\mathbf{X}$ about the origin is given by:
     $$
     \mathbb{E}[\mathbf{X}^n] = \int_{-\infty}^{\infty} x^n f_{\mathbf{X}}(x) \mathrm{d}x
     $$
     A particularly important case is the second moment (variance), which measures the dispersion of $\mathbf{X}$ around its mean.  
     随机变量$\mathbf{X}$关于原点的第$n$阶矩为：
     $$
     \mathbb{E}[\mathbf{X}^n] = \int_{-\infty}^{\infty} x^n f_{\mathbf{X}}(x) \mathrm{d}x
     $$
     特别重要的一个例子是二阶矩（方差），它衡量了$\mathbf{X}$围绕其均值的分散程度。

5. **Covariance**｜协方差:
   - For two random variables $\mathbf{X}$ and $\mathbf{Y}$, the covariance is defined as:

     $$
     \mathrm{Cov}(\mathbf{X}, \mathbf{Y}) = \mathbb{E}[(\mathbf{X} - \mathbb{E}[\mathbf{X}])(\mathbf{Y} - \mathbb{E}[\mathbf{Y}])]
     $$

     It measures the joint variability of $\mathbf{X}$ and $\mathbf{Y}$.

     对于两个随机变量$\mathbf{X}$和$\mathbf{Y}$，协方差定义为：

     $$
     \mathrm{Cov}(\mathbf{X}, \mathbf{Y}) = \mathbb{E}[(\mathbf{X} - \mathbb{E}[\mathbf{X}])(\mathbf{Y} - \mathbb{E}[\mathbf{Y}])]
     $$

     它衡量了$\mathbf{X}$和$\mathbf{Y}$的联合变化。

6. **Variance**｜方差:
   - The variance of a random variable $\mathbf{X}$, denoted by $\mathrm{Var}(\mathbf{X})$, is given by:

     $$
     \mathrm{Var}(\mathbf{X}) = \mathbb{E}[(\mathbf{X} - \mathbb{E}[\mathbf{X}])^2]
     $$

     It measures the spread of $\mathbf{X}$'s values around the mean.

     随机变量$\mathbf{X}$的方差，记作$\mathrm{Var}(\mathbf{X})$，定义为：
     $$
     \mathrm{Var}(\mathbf{X}) = \mathbb{E}[(\mathbf{X} - \mathbb{E}[\mathbf{X}])^2]
     $$

     它衡量了$\mathbf{X}$的取值围绕均值的分散程度。

## Calculation Techniques｜计算技巧

1. **Using Symmetry**｜利用对称性:
   - If the distribution of $\mathbf{X}$ is symmetric about $a$, then $\mathbb{E}[\mathbf{X}] = a$.  
     如果$\mathbf{X}$的分布关于$a$对称，那么$\mathbb{E}[\mathbf{X}] = a$。

2. **Indicator Variables**｜指示变量:
   - If $I_A$ is an indicator variable for event $A$, then $\mathbb{E}[I_A] = P(A)$.  
     如果$I_A$是事件$A$的指示变量，那么$\mathbb{E}[I_A] = P(A)$。

3. **Transformation**｜变换:
   - For $\mathbf{Y} = a\mathbf{X} + b$, use linearity:

$$
\mathbb{E}[\mathbf{Y}] = a\mathbb{E}[\mathbf{X}] + b
$$

     对于$\mathbf{Y} = a\mathbf{X} + b

$，利用线性性质：

     $$
     \mathbb{E}[\mathbf{Y}] = a\mathbb{E}[\mathbf{X}] + b
     $$

4. **Expected Value of Geometric Distribution**｜几何分布的期望:
   - If $\mathbf{X} \sim \text{Geom}(p)$:

     $$
     \mathbb{E}[\mathbf{X}] = \frac{1}{p}
     $$

     如果$\mathbf{X} \sim \text{Geom}(p)$：

     $$
     \mathbb{E}[\mathbf{X}] = \frac{1}{p}
     $$

5. **Moment Generating Functions**｜矩生成函数:
   - The moment generating function $M_{\mathbf{X}}(t)$ of a random variable $\mathbf{X}$ is defined as $M_{\mathbf{X}}(t) = \mathbb{E}[e^{t\mathbf{X}}]$. The $n$-th moment of $\mathbf{X}$ can be obtained by differentiating $M_{\mathbf{X}}(t)$ $n$ times and evaluating at $t=0$.  
     随机变量$\mathbf{X}$的矩生成函数$M_{\mathbf{X}}(t)$定义为$M_{\mathbf{X}}(t) = \mathbb{E}[e^{t\mathbf{X}}]$。$\mathbf{X}$的第$n$阶矩可以通过对$M_{\mathbf{X}}(t)$求$n$次导数并在$t=0$处进行求值得到。

6. **Expectation of Product of Independent Random Variables**｜独立随机变量乘积的期望:
   - If $\mathbf{X}$ and $\mathbf{Y}$ are independent, then:

     $$
     \mathbb{E}[\mathbf{X}\mathbf{Y}] = \mathbb{E}[\mathbf{X}] \mathbb{E}[\mathbf{Y}]
     $$

     如果$\mathbf{X}$和$\mathbf{Y}$是独立的，那么：

     $$
     \mathbb{E}[\mathbf{X}\mathbf{Y}] = \mathbb{E}[\mathbf{X}] \mathbb{E}[\mathbf{Y}]
     $$