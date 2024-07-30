# 概率密度函数和概率质量函数 Probability Density Function & Probability Mass Function

## 概率密度函数 (PDF)

### 定义

**概率密度函数 (Probability Density Function, PDF)** 是描述连续 [[Random Variables#随机变量 (Random Variables)]] 在某一特定值附近的概率分布的函数。给定连续随机变量 $X$，其概率密度函数记为 $f_X(x)$。PDF 满足以下性质：

1. $f_X(x) \geq 0$ 对于所有 $x \in \mathbb{R}$
2. $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$
3. 对于任意区间 $[a, b]$，$P(a \leq X \leq b) = \int_a^b f_X(x) \, dx$

### 常见分布的 PDF

- **正态分布 (Normal Distribution)**

$$
f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
$$

  其中，$\mu$ 为均值，$\sigma^2$ 为方差

- **指数分布 (Exponential Distribution)**

$$
f_X(x) = \lambda \exp(-\lambda x) \quad \text{for } x \geq 0
$$

  其中，$\lambda > 0$ 为速率参数

### 性质

- PDF 的值可以大于 1，但其积分值必须为 1
- 对于离散随机变量，PDF 的概念不适用，需要使用概率质量函数 (PMF)

## 概率质量函数 (PMF)

### 定义

**概率质量函数 (Probability Mass Function, PMF)** 是描述离散随机变量取某一特定值的概率的函数。给定离散随机变量 $X$，其概率质量函数记为 $p_X(x)$。PMF 满足以下性质：

1. $0 \leq p_X(x) \leq 1$ 对于所有 $x \in \mathbb{R}$
2. $\sum_{x \in \mathbb{X}} p_X(x) = 1$ 其中 $\mathbb{X}$ 是 $X$ 可能取值的集合

### 常见分布的 PMF

- **二项分布 (Binomial Distribution)**

$$
p_X(k) = \binom{n}{k} p^k (1-p)^{n-k} \quad \text{for } k = 0, 1, 2, \ldots, n
$$

  其中，$n$ 为试验次数，$p$ 为每次试验成功的概率

- **泊松分布 (Poisson Distribution)**

$$
p_X(k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for } k = 0, 1, 2, \ldots
$$

  其中，$\lambda$ 为平均发生率

### 性质

- PMF 的值总是在 $[0, 1]$ 之间
- 对于连续随机变量，PMF 的概念不适用，需要使用概率密度函数 (PDF)

## PDF 与 PMF 的区别

- PDF 适用于连续随机变量，而 PMF 适用于离散随机变量
- PDF 的积分为 1，而 PMF 的和为 1
- PDF 可以取值大于 1，但 PMF 只能在 $[0, 1]$ 之间

## 计算技巧

- 使用累积分布函数 (CDF) 简化概率计算，CDF $F_X(x)$ 定义为随机变量 $X$ 小于或等于 $x$ 的概率
  - 对于连续随机变量：$F_X(x) = \int_{-\infty}^x f_X(t) \, dt$
  - 对于离散随机变量：$F_X(x) = \sum_{t \leq x} p_X(t)$

- 随机变量换元：对于随机变量 $X$ 和 $Y = g(X)$，有 $F_X(x) = F_Y(g(x))|g'(x)|$

## 容易混淆的点

- **连续 vs 离散**：确保在使用 PDF 和 PMF 时区分随机变量的类型
- **PDF 值大于 1**：PDF 的值可以大于 1，但其积分必须为 1
- **求概率**：对于连续变量，用积分求概率；对于离散变量，用求和求概率
