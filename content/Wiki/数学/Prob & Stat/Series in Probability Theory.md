# 概率论级数公式 | Series in Probability Theory

## 均匀分布 | Uniform Distribution

### 概率质量函数 | Probability Mass Function

$$
p_X(x) = \frac{1}{n} \quad \text{for} \ x = 1, 2, \ldots, n
$$

### 期望值 | Expectation

$$
\mathbb{E}(X) = \sum_{x=1}^{n} x p_X(x) = \sum_{x=1}^{n} x \cdot \frac{1}{n} = \frac{1}{n} \sum_{x=1}^{n} x
$$

使用等差数列求和公式：

$$
\sum_{x=1}^{n} x = \frac{n(n+1)}{2}
$$

因此，

$$
\mathbb{E}(X) = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2}
$$

### 方差 | Variance

$$
\mathrm{Var}(X) = \sum_{x=1}^{n} (x - \mathbb{E}(X))^2 p_X(x)
$$

使用离散型均匀分布的方差公式：

$$
\mathrm{Var}(X) = \frac{(n^2 - 1)}{12}
$$

## 伯努利分布 | Bernoulli Distribution

### 概率质量函数 | Probability Mass Function

$$
p_X(x) = \begin{cases} 
p & \text{if} \ x = 1 \\
1 - p & \text{if} \ x = 0 
\end{cases}
$$

其中，$0 \leq p \leq 1$

where $0 \leq p \leq 1$

### 期望值 | Expectation

$$
\mathbb{E}(X) = \sum_{x \in \{0, 1\}} x p_X(x) = 0 \cdot (1 - p) + 1 \cdot p = p
$$

### 方差 | Variance

$$
\mathrm{Var}(X) = \sum_{x \in \{0, 1\}} (x - \mathbb{E}(X))^2 p_X(x) = (0 - p)^2 (1 - p) + (1 - p)^2 p = p(1 - p)
$$

## 二项分布 | Binomial Distribution

### 概率质量函数 | Probability Mass Function

$$
p_X(k) = \binom{n}{k} p^k (1 - p)^{n - k} \quad \text{for} \ k = 0, 1, 2, \ldots, n
$$

其中，$\binom{n}{k} = \frac{n!}{k!(n - k)!}$

where $\binom{n}{k} = \frac{n!}{k!(n - k)!}$

### 期望值 | Expectation

$$
\mathbb{E}(X) = \sum_{k = 0}^{n} k \binom{n}{k} p^k (1 - p)^{n - k} = np
$$

### 方差 | Variance

$$
\mathrm{Var}(X) = \sum_{k = 0}^{n} (k - np)^2 \binom{n}{k} p^k (1 - p)^{n - k} = np(1 - p)
$$

## 几何分布 | Geometric Distribution

### 概率质量函数 | Probability Mass Function

$$
p_X(k) = (1 - p)^{k - 1} p \quad \text{for} \ k = 1, 2, 3, \ldots
$$

### 期望值 | Expectation

$$
\mathbb{E}(X) = \sum_{k = 1}^{\infty} k (1 - p)^{k - 1} p
$$

求和过程：

$$
\begin{align*}
\mathbb{E}(X) &= \sum_{k = 1}^{\infty} k (1 - p)^{k - 1} p \\
&= p \sum_{k = 1}^{\infty} k (1 - p)^{k - 1} \\
\text{令} \ q &= 1 - p \\
\mathbb{E}(X) &= p \sum_{k = 1}^{\infty} k q^{k - 1} \\
\text{使用等比级数求和公式} \ \sum_{k = 1}^{\infty} k q^{k - 1} &= \frac{1}{(1 - q)^2} \\
\mathbb{E}(X) &= p \cdot \frac{1}{(1 - q)^2} = p \cdot \frac{1}{p^2} = \frac{1}{p}
\end{align*}
$$

### 方差 | Variance

$$
\mathrm{Var}(X) = \sum_{k = 1}^{\infty} \left(k - \mathbb{E}(X)\right)^2 (1 - p)^{k - 1} p = \sum_{k = 1}^{\infty} \left(k - \frac{1}{p}\right)^2 (1 - p)^{k - 1} p
$$

#### 计算过程 | Calculation Process

1. 展开平方项

$$
\begin{align*}
\mathrm{Var}(X) &= \sum_{k = 1}^{\infty} \left(k^2 - 2k \cdot \frac{1}{p} + \frac{1}{p^2}\right) (1 - p)^{k - 1} p \\
&= \sum_{k = 1}^{\infty} \left(k^2 (1 - p)^{k - 1} p - 2k \cdot \frac{1}{p} (1 - p)^{k - 1} p + \frac{1}{p^2} (1 - p)^{k - 1} p\right) \\
&= p \left[\sum_{k = 1}^{\infty} k^2 (1 - p)^{k - 1} - 2 \cdot \frac{1}{p} \sum_{k = 1}^{\infty} k (1 - p)^{k - 1} + \frac{1}{p^2} \sum_{k = 1}^{\infty} (1 - p)^{k - 1}\right]
\end{align*}
$$

2. 分别计算三个部分

第一部分：

$$
\sum_{k = 1}^{\infty} k^2 (1 - p)^{k - 1}
$$

利用公式 $\sum_{k = 1}^{\infty} k^2 q^{k - 1} = \frac{1 + q}{(1 - q)^3}$ 其中 $q = 1 - p$

$$
\sum_{k = 1}^{\infty} k^2 (1 - p)^{k - 1} = \frac{1 + (1 - p)}{(1 - (1 - p))^3} = \frac{2 - p}{p^3}
$$

第二部分：

$$
\sum_{k = 1}^{\infty} k (1 - p)^{k - 1}
$$

利用公式 $\sum_{k = 1}^{\infty} k q^{k - 1} = \frac{1}{(1 - q)^2}$ 其中 $q = 1 - p$

$$
\sum_{k = 1}^{\infty} k (1 - p)^{k - 1} = \frac{1}{p^2}
$$

第三部分：

$$
\sum_{k = 1}^{\infty} (1 - p)^{k - 1}
$$

这是一个无穷等比数列，求和结果为：

$$
\sum_{k = 1}^{\infty} (1 - p)^{k - 1} = \frac{1}{1 - (1 - p)} = \frac{1}{p}
$$

3. 综合计算方差

$$
\begin{align*}
\mathrm{Var}(X) &= p \left[\frac{2 - p}{p^3} - 2 \cdot \frac{1}{p} \cdot \frac{1}{p^2} + \frac{1}{p^2} \cdot \frac{1}{p}\right] \\
&= p \left[\frac{2 - p}{p^3} - \frac{2}{p^3} + \frac{1}{p^3}\right] \\
&= p \left[\frac{2 - p - 2 + 1}{p^3}\right] \\
&= p \left[\frac{-p + 1}{p^3}\right] \\
&= \frac{1 - p}{p^2}
\end{align*}
$$

综上所述，几何分布的方差为：

$$
\mathrm{Var}(X) = \frac{1 - p}{p^2}
$$

## 泊松分布 | Poisson Distribution

### 概率质量函数 | Probability Mass Function

$$
p_X(k) = \frac{\lambda^k e^{-\lambda}}{k!} \quad \text{for} \ k = 0, 1, 2, \ldots
$$

### 期望值 | Expectation

$$
\mathbb{E}(X) = \sum_{k = 0}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} = \lambda
$$

求和过程：

$$
\begin{align*}
\mathbb{E}(X) &= \sum_{k = 0}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} \\
\text{令} \ p(k) &= \frac{\lambda^k e^{-\lambda}}{k!} \\
\mathbb{E}(X) &= \sum_{k = 1}^{\infty}

 k p(k) \\
&= \sum_{k = 1}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} \\
&= \sum_{k = 1}^{\infty} \lambda \frac{\lambda^{k-1} e^{-\lambda}}{(k-1)!} \\
&= \lambda \sum_{k = 0}^{\infty} \frac{\lambda^k e^{-\lambda}}{k!} \\
&= \lambda \cdot 1 = \lambda
\end{align*}
$$

### 方差 | Variance

$$
\mathrm{Var}(X) = \sum_{k = 0}^{\infty} (k - \lambda)^2 \frac{\lambda^k e^{-\lambda}}{k!} = \lambda
$$

求和过程：

$$
\begin{align*}
\mathrm{Var}(X) &= \sum_{k = 0}^{\infty} (k - \lambda)^2 \frac{\lambda^k e^{-\lambda}}{k!} \\
&= \sum_{k = 0}^{\infty} (k^2 - 2k\lambda + \lambda^2) \frac{\lambda^k e^{-\lambda}}{k!} \\
&= \sum_{k = 0}^{\infty} k^2 \frac{\lambda^k e^{-\lambda}}{k!} - 2\lambda \sum_{k = 0}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} + \lambda^2 \sum_{k = 0}^{\infty} \frac{\lambda^k e^{-\lambda}}{k!} \\
\text{第一项:} \\
\sum_{k = 0}^{\infty} k^2 \frac{\lambda^k e^{-\lambda}}{k!} &= \lambda \sum_{k = 1}^{\infty} k \frac{\lambda^{k-1} e^{-\lambda}}{(k-1)!} \\
&= \lambda \sum_{k = 0}^{\infty} (k + 1) \frac{\lambda^k e^{-\lambda}}{k!} \\
&= \lambda \left[ \sum_{k = 0}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} + \sum_{k = 0}^{\infty} \frac{\lambda^k e^{-\lambda}}{k!} \right] \\
&= \lambda (\lambda + 1) \\
&= \lambda^2 + \lambda \\
\text{第二项:} \\
-2\lambda \sum_{k = 0}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} &= -2\lambda \lambda \\
&= -2\lambda^2 \\
\text{第三项:} \\
\lambda^2 \sum_{k = 0}^{\infty} \frac{\lambda^k e^{-\lambda}}{k!} &= \lambda^2 \cdot 1 \\
&= \lambda^2 \\
\mathrm{Var}(X) &= \lambda^2 + \lambda - 2\lambda^2 + \lambda^2 \\
&= \lambda
\end{align*}
$$
