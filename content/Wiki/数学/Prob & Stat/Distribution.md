# Distribution 分布

## 1. Uniform Distribution 均匀分布

### Definition 定义

The uniform distribution describes an equal probability for all outcomes in a given range. In the case of a continuous uniform distribution, the probability density function (PDF) is constant between the lower bound $a$ and the upper bound $b$.

均匀分布描述了在给定范围内所有结果的等概率。在连续均匀分布的情况下，概率密度函数（PDF）在下限 $a$ 和上限 $b$ 之间是恒定的。

$$
f(x) = \begin{cases} 
\frac{1}{b-a} & \text{if } a \leq x \leq b \\
0 & \text{otherwise}
\end{cases}
$$

### Properties 性质

- Mean 平均值: $\mu = \frac{a + b}{2}$
- Variance 方差: $\sigma^2 = \frac{(b - a)^2}{12}$
- Cumulative Distribution Function (CDF) 累积分布函数 (CDF):

$$
F(x) = \begin{cases} 
0 & \text{if } x < a \\
\frac{x - a}{b - a} & \text{if } a \leq x \leq b \\
1 & \text{if } x > b
\end{cases}
$$

## 2. Normal Distribution 正态分布

### Definition 定义

The normal distribution, also known as the Gaussian distribution, is a continuous probability distribution characterized by a bell-shaped curve. It is defined by its mean $\mu$ and variance $\sigma^2$.

正态分布，也称为高斯分布，是一种连续概率分布，其特征是钟形曲线。它由其平均值 $\mu$ 和方差 $\sigma^2$ 定义。

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)
$$

### Properties 性质

- Mean 平均值: $\mu$
- Variance 方差: $\sigma^2$
- Standard Normal Distribution 标准正态分布: $\mu = 0, \sigma^2 = 1$
- The 68-95-99.7 Rule 68-95-99.7 规则: Approximately 68% of the data falls within 1 standard deviation, 95% within 2 standard deviations, and 99.7% within 3 standard deviations.

## 3. Exponential Distribution 指数分布

### Definition 定义

The exponential distribution is a continuous probability distribution that describes the time between events in a Poisson process. It is defined by a single parameter $\lambda$, which is the rate parameter.

指数分布是一种连续概率分布，描述了泊松过程中文件之间的时间。它由一个参数 $\lambda$ 定义，即速率参数。

$$
f(x) = \lambda \exp(-\lambda x) \quad \text{for } x \geq 0
$$

### Properties 性质

- Mean 平均值: $\mu = \frac{1}{\lambda}$
- Variance 方差: $\sigma^2 = \frac{1}{\lambda^2}$
- Memoryless Property 无记忆性: $P(X > x + t \mid X > t) = P(X > x)$

## 4. Binomial Distribution 二项分布

### Definition 定义

The binomial distribution describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success $p$.

二项分布描述了在固定数量的独立伯努利试验中成功的次数，每个试验都有相同的成功概率 $p$。

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

### Properties 性质

- Mean 平均值: $\mu = np$
- Variance 方差: $\sigma^2 = np(1-p)$
- If $X \sim \text{Binomial}(n, p)$ and $n$ is large, $X$ can be approximated by a normal distribution with mean $np$ and variance $np(1-p)$.

## 5. Poisson Distribution 泊松分布

### Definition 定义

The Poisson distribution describes the number of events occurring in a fixed interval of time or space, given the events occur with a known constant mean rate $\lambda$ and independently of the time since the last event.

泊松分布描述了在固定时间或空间间隔内发生的事件数量，假定事件以已知的恒定平均速率 $\lambda$ 发生，并且与上次事件发生的时间无关。

$$
P(X = k) = \frac{\lambda^k \exp(-\lambda)}{k!}
$$

### Properties 性质

- Mean 平均值: $\mu = \lambda$
- Variance 方差: $\sigma^2 = \lambda$
- If $X \sim \text{Poisson}(\lambda)$, then $X$ is approximately normally distributed with mean $\lambda$ and variance $\lambda$ when $\lambda$ is large.

## 6. Geometric Distribution 几何分布

### Definition 定义

The geometric distribution describes the number of trials needed to get the first success in repeated Bernoulli trials, each with the same probability of success $p$.

几何分布描述了在重复的伯努利试验中达到第一次成功所需的试验次数，每次试验都有相同的成功概率 $p$。

$$
P(X = k) = (1-p)^{k-1} p \quad \text{for } k = 1, 2, 3, \ldots
$$

### Properties 性质

- Mean 平均值: $\mu = \frac{1}{p}$
- Variance 方差: $\sigma^2 = \frac{1-p}{p^2}$
- Memoryless Property 无记忆性: $P(X > k + n \mid X > n) = P(X > k)$

## Summary 总结

Understanding different types of distributions is crucial for statistical analysis and probability theory. Each distribution has its own unique properties and applications, making them suitable for various types of data and scenarios.

了解不同类型的分布对于统计分析和概率论非常重要。每种分布都有其独特的性质和应用，使其适用于各种类型的数据和场景。
