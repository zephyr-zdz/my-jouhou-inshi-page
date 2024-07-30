# 随机变量 (Random Variables)

## 定义 (Definition)

**随机变量**是一种函数，定义在一个样本空间上，并映射到实数。通常用大写字母表示，例如 $X$、$Y$。随机变量可以分为离散随机变量和连续随机变量。

A **random variable** is a function defined on a sample space that maps outcomes to real numbers. It is usually denoted by uppercase letters, such as $X$ and $Y$. Random variables can be categorized into discrete random variables and continuous random variables.

## 离散随机变量 (Discrete Random Variables)

### 定义 (Definition)

如果一个随机变量只能取有限个或可数无限个不同的值，则称为离散随机变量。

A random variable is called a discrete random variable if it can take on a finite or countably infinite number of distinct values.

### 例子 (Examples)

- 掷骰子的点数
- 抛硬币的正反面

- The number shown on a rolled die
- The outcome of a coin toss

### 概率质量函数 (Probability Mass Function, PMF)

离散随机变量 $X$ 的概率质量函数 (PMF) 定义为 $P(X=x_i)=p_i$，其中 $x_i$ 是 $X$ 的可能取值，$p_i$ 是 $X$ 取值 $x_i$ 的概率。

The probability mass function (PMF) of a discrete random variable $X$ is defined as $P(X=x_i)=p_i$, where $x_i$ is a possible value of $X$, and $p_i$ is the probability that $X$ takes the value $x_i$.

### 累积分布函数 (Cumulative Distribution Function, CDF)

离散随机变量 $X$ 的累积分布函数 (CDF) 定义为 $F(x)=P(X \leq x)$。

The cumulative distribution function (CDF) of a discrete random variable $X$ is defined as $F(x)=P(X \leq x)$.

### 期望值和方差 (Expectation and Variance)

- 期望值 (Expectation): $E(X) = \sum_{i} x_i P(X = x_i)$
- 方差 (Variance): $\text{Var}(X) = E[(X - E(X))^2] = \sum_{i} (x_i - E(X))^2 P(X = x_i)$

- Expectation: $E(X) = \sum_{i} x_i P(X = x_i)$
- Variance: $\text{Var}(X) = E[(X - E(X))^2] = \sum_{i} (x_i - E(X))^2 P(X = x_i)$

## 连续随机变量 (Continuous Random Variables)

### 定义 (Definition)

如果一个随机变量可以取任何实数值，则称为连续随机变量。

A random variable is called a continuous random variable if it can take on any real value.

### 例子 (Examples)

- 测量长度、时间、温度

- Measuring length, time, temperature

### 概率密度函数 (Probability Density Function, PDF)

连续随机变量 $X$ 的概率密度函数 (PDF) 定义为 $f_X(x)$，满足 $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$。任意区间 $[a, b]$ 上的概率为 $P(a \leq X \leq b) = \int_{a}^{b} f_X(x) \, dx$。

The probability density function (PDF) of a continuous random variable $X$ is defined as $f_X(x)$, such that $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$. The probability over any interval $[a, b]$ is given by $P(a \leq X \leq b) = \int_{a}^{b} f_X(x) \, dx$.

### 累积分布函数 (Cumulative Distribution Function, CDF)

连续随机变量 $X$ 的累积分布函数 (CDF) 定义为 $F(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t) \, dt$。

The cumulative distribution function (CDF) of a continuous random variable $X$ is defined as $F(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t) \, dt$.

### 期望值和方差 (Expectation and Variance)

- 期望值 (Expectation): $E(X) = \int_{-\infty}^{\infty} x f_X(x) \, dx$
- 方差 (Variance): $\text{Var}(X) = E[(X - E(X))^2] = \int_{-\infty}^{\infty} (x - E(X))^2 f_X(x) \, dx$

- Expectation: $E(X) = \int_{-\infty}^{\infty} x f_X(x) \, dx$
- Variance: $\text{Var}(X) = E[(X - E(X))^2] = \int_{-\infty}^{\infty} (x - E(X))^2 f_X(x) \, dx$

## 常见分布 (Common Distributions)

### 离散分布 (Discrete Distributions)

- **二项分布 (Binomial Distribution)**: $X \sim \text{Bin}(n, p)$
  - PMF: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
  - 期望值: $E(X) = np$
  - 方差: $\text{Var}(X) = np(1-p)$

- **泊松分布 (Poisson Distribution)**: $X \sim \text{Poisson}(\lambda)$
  - PMF: $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$
  - 期望值: $E(X) = \lambda$
  - 方差: $\text{Var}(X) = \lambda$

### 连续分布 (Continuous Distributions)

- **正态分布 (Normal Distribution)**: $X \sim N(\mu, \sigma^2)$
  - PDF: $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
  - 期望值: $E(X) = \mu$
  - 方差: $\text{Var}(X) = \sigma^2$

- **指数分布 (Exponential Distribution)**: $X \sim \text{Exp}(\lambda)$
  - PDF: $f_X(x) = \lambda e^{-\lambda x}$ for $x \geq 0$
  - 期望值: $E(X) = \frac{1}{\lambda}$
  - 方差: $\text{Var}(X) = \frac{1}{\lambda^2}$

## 注意事项 (Important Points to Remember)

- 随机变量的期望值和方差计算时需要特别注意积分或求和的范围和条件。
- 概率质量函数 (PMF) 适用于离散随机变量，概率密度函数 (PDF) 适用于连续随机变量。
- 累积分布函数 (CDF) 无论是离散还是连续随机变量都适用。
