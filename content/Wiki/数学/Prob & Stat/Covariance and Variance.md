1# Variance and Covariance 方差与协方差

## 1. Definitions 定义

### Variance 方差

**Variance** measures how much a set of numbers is spread out. It is the expectation of the squared deviation of a random variable from its mean.

**方差**度量一组数据的分散程度。它是随机变量与其均值的平方偏差的期望。

$$
\mathrm{Var}(\mathbf{X}) = \mathbb{E}\left[(\mathbf{X} - \mu)^2\right]
$$

Where:

- $\mathbf{X}$ is a random variable
- $\mu$ is the mean of $\mathbf{X}$
- $\mathbb{E}$ denotes the expectation

其中:

- $\mathbf{X}$ 是随机变量
- $\mu$ 是 $\mathbf{X}$ 的均值
- $\mathbb{E}$ 表示期望

### Covariance 协方差

**Covariance** measures the directional relationship between two random variables. It indicates the extent to which the variables change together.

**协方差**度量两个随机变量之间的方向关系。它表明变量共同变化的程度。

$$
\mathrm{Cov}(\mathbf{X}, \mathbf{Y}) = \mathbb{E}\left[(\mathbf{X} - \mathbb{E}[\mathbf{X}])(\mathbf{Y} - \mathbb{E}[\mathbf{Y}])\right]
$$

Where:

- $\mathbf{X}, \mathbf{Y}$ are random variables
- $\mathbb{E}$ denotes the expectation

其中:

- $\mathbf{X}, \mathbf{Y}$ 是随机变量
- $\mathbb{E}$ 表示期望

## 2. Important Properties 重要性质

### Variance Properties 方差性质

1. **Non-Negative** 非负性:

$$
   \mathrm{Var}(\mathbf{X}) \geq 0
$$

2. **Zero Variance** 零方差:

$$
   \mathrm{Var}(\mathbf{X}) = 0 \implies \mathbf{X} \text{ is constant}
$$

3. **Variance of a Constant** 常数的方差:

$$
   \mathrm{Var}(c) = 0
$$

4. **Scaling Property** 缩放性质:

$$
   \mathrm{Var}(a\mathbf{X}) = a^2 \mathrm{Var}(\mathbf{X})
$$

5. **Sum of Independent Variables** 独立变量和的方差:
   If $\mathbf{X}$ and $\mathbf{Y}$ are independent, then

$$
   \mathrm{Var}(\mathbf{X} + \mathbf{Y}) = \mathrm{Var}(\mathbf{X}) + \mathrm{Var}(\mathbf{Y})
$$

### Covariance Properties 协方差性质

1. **Symmetry** 对称性:

$$
   \mathrm{Cov}(\mathbf{X}, \mathbf{Y}) = \mathrm{Cov}(\mathbf{Y}, \mathbf{X})
$$

2. **Linearity** 线性性质:

$$
   \mathrm{Cov}(a\mathbf{X} + b, \mathbf{Y}) = a \mathrm{Cov}(\mathbf{X}, \mathbf{Y})
$$

3. **Covariance of a Variable with Itself** 自身的协方差:

$$
   \mathrm{Cov}(\mathbf{X}, \mathbf{X}) = \mathrm{Var}(\mathbf{X})
$$

4. **Sum of Covariances** 协方差的和:

$$
   \mathrm{Cov}(\mathbf{X} + \mathbf{Y}, \mathbf{Z}) = \mathrm{Cov}(\mathbf{X}, \mathbf{Z}) + \mathrm{Cov}(\mathbf{Y}, \mathbf{Z})
$$

## 3. Inferences 推断

### Variance Inferences 方差推断

- **Population Variance** 总体方差:
  Population variance is usually unknown and needs to be estimated from sample data.

  **总体方差**通常未知，需要通过样本数据进行估计。

- **Sample Variance** 样本方差:

$$
  s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \overline{x})^2
$$

  where $x_i$ are sample values and $\overline{x}$ is the sample mean.

  其中 $x_i$ 是样本值，$\overline{x}$ 是样本均值。

### Covariance Inferences 协方差推断

- **Population Covariance** 总体协方差:
  Similar to population variance, population covariance is usually unknown and needs to be estimated.

  类似于总体方差，总体协方差通常未知，需要进行估计。

- **Sample Covariance** 样本协方差:

$$
  s_{XY} = \frac{1}{n-1} \sum_{i=1}^n (x_i - \overline{x})(y_i - \overline{y})
$$

  where $x_i, y_i$ are sample values and $\overline{x}, \overline{y}$ are sample means.

  其中 $x_i, y_i$ 是样本值，$\overline{x}, \overline{y}$ 是样本均值。

### 期望 $\mathbb{E}\left( (\bar{X} - \mu)^2 \right) = \frac{\sigma^2}{n}$ 的推导 Derivation of $\mathbb{E}\left( (\bar{X} - \mu)^2 \right) = \frac{\sigma^2}{n}$

1. **定义样本均值：Definition of the Sample Mean**

   样本均值 $\bar{X}$ 定义为：

   The sample mean $\bar{X}$ is defined as:

   $$
   \bar{X} = \frac{1}{n} \sum_{i=1}^n X_i

$$


2. **样本均值的期望：Expectation of the Sample Mean**

   样本均值 $\bar{X}$ 的期望 $\mathbb{E}(\bar{X})$ 是总体均值 $\mu$：

   The expectation of the sample mean $\bar{X}$ is the population mean $\mu$:

   $$

   \mathbb{E}(\bar{X}) = \mu

$$

3. **计算 $\mathbb{E}\left( (\bar{X} - \mu)^2 \right)$：Calculating $\mathbb{E}\left( (\bar{X} - \mu)^2 \right)$**

   我们需要计算 $\mathbb{E}\left( (\bar{X} - \mu)^2 \right)$。注意到 $\bar{X}$ 是 $X_1, X_2, \ldots, X_n$ 的线性组合，因此我们可以利用方差的性质：

   We need to calculate $\mathbb{E}\left( (\bar{X} - \mu)^2 \right)$. Noting that $\bar{X}$ is a linear combination of $X_1, X_2, \ldots, X_n$, we can use the properties of variance:

   $$

   \text{Var}(\bar{X}) = \text{Var}\left( \frac{1}{n} \sum_{i=1}^n X_i \right)

$$

4. **方差的性质：Properties of Variance**

   利用方差的性质，对于独立同分布的随机变量 $X_i$，我们有：

   Using the properties of variance, for i.i.d. random variables $X_i$, we have:

   $$

   \text{Var}\left( \frac{1}{n} \sum_{i=1}^n X_i \right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{1}{n^2} \cdot n \sigma^2 = \frac{\sigma^2}{n}

$$

5. **利用方差的定义：Using the Definition of Variance**

   方差的定义是 $\text{Var}(X) = \mathbb{E}\left[ (X - \mathbb{E}(X))^2 \right]$，所以：

   The definition of variance is $\text{Var}(X) = \mathbb{E}\left[ (X - \mathbb{E}(X))^2 \right]$, thus:

   $$

   \text{Var}(\bar{X}) = \mathbb{E}\left[ (\bar{X} - \mathbb{E}(\bar{X}))^2 \right] = \mathbb{E}\left[ (\bar{X} - \mu)^2 \right]

$$

6. **结合方差的结果：Combining the Variance Result**

   因此，我们有：

   Therefore, we have:

   $$

   \mathbb{E}\left( (\bar{X} - \mu)^2 \right) = \text{Var}(\bar{X}) = \frac{\sigma^2}{n}

$$

### The Derivation of Unbiased Estimator for Sample Variance 样本方差无偏估计的推导

Assume we have a random variable $X$ with population mean $\mu$ and population variance $\sigma^2$. A sample of size $n$, $X_1, X_2, \ldots, X_n$, is drawn from the population, with sample mean $\bar{X}$ and sample variance $s^2$ defined as:

假设我们有一个随机变量 $X$，其总体均值为 $\mu$，总体方差为 $\sigma^2$。从总体中抽取一个样本 $X_1, X_2, \ldots, X_n$，样本均值为 $\bar{X}$，样本方差 $s^2$ 定义为：

$$

 s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2

$$

We need to prove that $\mathbb{E}(s^2) = \sigma^2$, meaning that the sample variance $s^2$ is an unbiased estimator of the population variance $\sigma^2$.

我们需要证明 $\mathbb{E}(s^2) = \sigma^2$，即样本方差 $s^2$ 是总体方差 $\sigma^2$ 的无偏估计。

1. **样本方差的展开：Expansion of Sample Variance**

$$

   s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2

$$

   首先展开 $\sum_{i=1}^n (X_i - \bar{X})^2$：

   First, expand $\sum_{i=1}^n (X_i - \bar{X})^2$:

$$

   \sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n \left[ (X_i - \mu) - (\bar{X} - \mu) \right]^2

$$

$$

   = \sum_{i=1}^n (X_i - \mu)^2 - 2 \sum_{i=1}^n (X_i - \mu)(\bar{X} - \mu) + \sum_{i=1}^n (\bar{X} - \mu)^2

$$

2. **处理中间项：Handling the Middle Term**
   由于 $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$，我们可以得到：
   Since $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$, we can get:

$$

   \sum_{i=1}^n (X_i - \mu)(\bar{X} - \mu) = (\bar{X} - \mu) \sum_{i=1}^n (X_i - \mu)

$$

   而 $\sum_{i=1}^n (X_i - \mu) = n (\bar{X} - \mu)$，所以：

   And $\sum_{i=1}^n (X_i - \mu) = n (\bar{X} - \mu)$, thus:

$$

   \sum_{i=1}^n (X_i - \mu)(\bar{X} - \mu) = n (\bar{X} - \mu)(\bar{X} - \mu) = n (\bar{X} - \mu)^2

$$

3. **代入展开公式：Substituting Back into the Expanded Formula**

$$

   \sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu)^2 - 2 n (\bar{X} - \mu)^2 + n (\bar{X} - \mu)^2

$$

$$

   = \sum_{i=1}^n (X_i - \mu)^2 - n (\bar{X} - \mu)^2

$$

4. **求期望：Taking the Expectation**
   现在我们计算 $s^2$ 的期望：
   Now we calculate the expectation of $s^2$:

$$

   \mathbb{E}(s^2) = \mathbb{E}\left( \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2 \right)

$$

$$

   = \frac{1}{n-1} \mathbb{E}\left( \sum_{i=1}^n (X_i - \mu)^2 - n (\bar{X} - \mu)^2 \right)

$$

5. **利用性质：Using Properties**
   $\mathbb{E}\left( \sum_{i=1}^n (X_i - \mu)^2 \right) = n \sigma^2$，以及 $\mathbb{E}\left( (\bar{X} - \mu)^2 \right) = \frac{\sigma^2}{n}$，所以：
   $\mathbb{E}\left( \sum_{i=1}^n (X_i - \mu)^2 \right) = n \sigma^2$ and $\mathbb{E}\left( (\bar{X} - \mu)^2 \right) = \frac{\sigma^2}{n}$ [[Covariance and Variance#期望 $ mathbb{E} left( ( bar{X} - mu) 2 right) = frac{ sigma 2}{n}$ 的推导 Derivation of $ mathbb{E} left( ( bar{X} - mu) 2 right) = frac{ sigma 2}{n}$|Here]] , so:

$$

   \mathbb{E}\left( \sum_{i=1}^n (X_i - \bar{X})^2 \right) = n \sigma^2 - n \cdot \frac{\sigma^2}{n} = n \sigma^2 - \sigma^2 = (n-1) \sigma^2

$$

6. **得到最终结果：Obtaining the Final Result**

$$

   \mathbb{E}(s^2) = \frac{1}{n-1} (n-1) \sigma^2 = \sigma^2

$$

因此，样本方差 $s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$ 是总体方差 $\sigma^2$ 的无偏估计。

Therefore, the sample variance $s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$ is an unbiased estimator of the population variance $\sigma^2$.
