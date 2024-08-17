# 大数定律与极限定理 | Laws of Large Numbers and Limit Theorems

## 常用概率不等式 | Common Probability Inequalities

在概率论中，不等式用于估计某一事件发生的概率上界。这些不等式在大数定律和极限定理的证明和应用中扮演着重要角色。常见的不等式包括马尔可夫不等式、切比雪夫不等式、赫芬丁不等式、和切尔诺夫界。

In probability theory, inequalities are used to estimate upper bounds on the probability of an event occurring. These inequalities play crucial roles in the proof and application of laws of large numbers and limit theorems. Common inequalities include Markov's Inequality, Chebyshev's Inequality, Hoeffding's Inequality, and the Chernoff Bound.

### 1. 马尔可夫不等式 | Markov's Inequality

**条件:** 适用于非负随机变量，即 $X \geq 0$。$\mathbb{E}[X]$ 存在。

**Condition:** Applicable to non-negative random variables, i.e., $X \geq 0$. The expectation $\mathbb{E}[X]$ exists.

马尔可夫不等式给出了随机变量 $X$ 超过某一阈值 $a$ 的概率上界。它仅依赖于期望值 $\mathbb{E}[X]$，忽略了随机变量的其他特征，如方差。

Markov's Inequality provides an upper bound on the probability that a random variable $X$ exceeds a certain threshold $a$. It only depends on the expectation $\mathbb{E}[X]$, ignoring other characteristics of the random variable, such as variance.

$$
\mathbb{P}(X \geq a) \leq \frac{\mathbb{E}[X]}{a}, \quad \text{for } a > 0.
$$

#### 指数形式的马尔可夫不等式 | Markov's Inequality in Exponential Form

当 $X$ 是任意随机变量（不一定是非负随机变量）时，马尔可夫不等式的另一种更通用的形式为指数形式。对于任意 $\lambda > 0$，不等式如下：

When $X$ is any random variable (not necessarily non-negative), a more general form of Markov's Inequality is the exponential form. For any $\lambda > 0$, the inequality is as follows:

$$
\mathbb{P}(X \geq a) \leq \inf_{\lambda > 0} \left\{\exp(-\lambda a) \mathbb{E}[\exp(\lambda X)]\right\}, \quad \text{for } a > 0.
$$

这个形式在处理具有指数尾部的随机变量（如正态分布、泊松分布）时尤为有用，因为它通过选择最优的 $\lambda$，可以显著提高不等式的紧度。

This form is particularly useful when dealing with random variables that have exponential tails (e.g., normal or Poisson distributions), as it allows for a significant improvement in the tightness of the inequality by selecting the optimal $\lambda$.

**紧度:** 马尔可夫不等式是相对宽松的，因为它只利用了随机变量的期望值信息。这意味着它在某些情况下可能给出一个较大的上界，特别是当随机变量的分布有较高方差时。相比之下，指数形式的马尔可夫不等式更加灵活和紧密，尤其在处理具有指数尾部的随机变量时，通过优化 $\lambda$ 能够获得更严格的概率上界。

**Tightness:** Markov's Inequality is relatively loose because it only uses the information of the expectation of the random variable. This means that it may provide a large upper bound in some cases, especially when the random variable has a high variance. In contrast, the exponential form of Markov's Inequality is more flexible and tighter, especially when dealing with random variables with exponential tails, as optimizing $\lambda$ can yield a more stringent upper bound.

因此，马尔可夫不等式通常在信息有限的情况下使用，如在只有期望值已知但方差或分布形状未知时。虽然该不等式上界较松，但它为更复杂的不等式（如切比雪夫不等式）奠定了基础。而指数形式则提供了在处理不同分布类型时更为强大的工具。

Therefore, Markov's Inequality is often used in situations with limited information, such as when only the expectation is known but variance or distribution shape is unknown. Although the upper bound provided by this inequality is loose, it lays the foundation for more complex inequalities (e.g., Chebyshev's Inequality). The exponential form, on the other hand, provides a more powerful tool when dealing with different types of distributions.

### 2. 切比雪夫不等式 | Chebyshev's Inequality

**条件:** 适用于任意具有有限期望 $\mu$ 和有限方差 $\sigma^2$ 的随机变量。

**Condition:** Applicable to any random variable with a finite expectation $\mu$ and finite variance $\sigma^2$.

$$
\mathbb{P}(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}, \quad \text{for } k > 0.
$$

**紧度:** 切比雪夫不等式比马尔可夫不等式更紧密，因为它考虑了方差的影响。然而，对于分布有较高峰度（如正态分布）的随机变量，它可能仍然不够紧密。

**Tightness:** Chebyshev's Inequality is tighter than Markov's because it takes variance into account. However, for distributions with high kurtosis (e.g., normal distribution), it may still be insufficiently tight.

### 3. 赫芬丁不等式 | Hoeffding's Inequality

**条件:** 适用于一列独立的、有界随机变量 $\{X_i\}$，即对于每个 $i$，$X_i$ 取值在区间 $[a_i, b_i]$ 内。

**Condition:** Applicable to a sequence of independent, bounded random variables $\{X_i\}$, where for each $i$, the value of $X_i$ lies within the interval $[a_i, b_i]$.

$$
\mathbb{P}\left(\overline{X}_n - \mathbb{E}[\overline{X}_n] \geq t \right) \leq \exp\left(-\frac{2n^2t^2}{\sum_{i=1}^{n}(b_i-a_i)^2}\right),
$$

其中 $\overline{X}_n = \frac{1}{n}\sum_{i=1}^{n}X_i$。

where $\overline{X}_n = \frac{1}{n}\sum_{i=1}^{n}X_i$.

**紧度:** 赫芬丁不等式是比切比雪夫不等式更紧密的概率上界，因为它利用了独立性和有界性的假设。它在应用于独立同分布（i.i.d.）的随机变量时特别有效。

**Tightness:** Hoeffding's Inequality provides a tighter upper bound than Chebyshev's because it utilizes the assumptions of independence and boundedness. It is particularly effective when applied to independent and identically distributed (i.i.d.) random variables.

### 4. 切尔诺夫界 | Chernoff Bound

**条件:** 适用于独立的二项分布随机变量或可以通过指数生成函数处理的随机变量。

**Condition:** Applicable to independent Bernoulli random variables or random variables that can be handled via moment-generating functions.

**上尾界 | Upper Tail Bound:**

$$
\mathbb{P}\left(S_n \geq (1+\delta)\mathbb{E}[S_n]\right) \leq \exp\left(-\frac{\delta^2 \mathbb{E}[S_n]}{2+\delta}\right),
$$

其中 $S_n = \sum_{i=1}^{n}X_i$，$\delta > 0$。

where $S_n = \sum_{i=1}^{n}X_i$ and $\delta > 0$.

**紧度:** 切尔诺夫界是最紧密的概率上界之一，尤其在处理大偏差时效果显著。它比赫芬丁不等式更强大，特别是当随机变量可以通过其指数生成函数来处理时。

**Tightness:** The Chernoff Bound is one of the tightest probability upper bounds, especially effective in dealing with large deviations. It is more powerful than Hoeffding's Inequality, particularly when random variables can be handled via their moment-generating functions.
