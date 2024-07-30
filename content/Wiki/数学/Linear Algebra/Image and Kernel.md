# Image and Kernel 值域和核

## Image / 值域

### Definition / 定义

The image (or range) of a linear transformation $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$ is the set of all vectors $\mathbf{y} \in \mathbb{R}^n$ that can be written as $T_{\mathbf{A}}(\mathbf{x}) = \mathbf{A}\mathbf{x}$ for some $\mathbf{x} \in \mathbb{R}^m$.

线性变换 $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$ 的值域（或范围）是所有可以写成 $T_{\mathbf{A}}(\mathbf{x}) = \mathbf{A}\mathbf{x}$ 形式的 $\mathbb{R}^n$ 中的向量 $\mathbf{y}$ 的集合，其中 $\mathbf{x} \in \mathbb{R}^m$。

$$
\mathrm{Im}(T_{\mathbf{A}}) = \{\mathbf{y} \in \mathbb{R}^n \mid \mathbf{y} = \mathbf{A}\mathbf{x} \text{ for some } \mathbf{x} \in \mathbb{R}^m\}
$$

### Properties / 性质

- The dimension of the image of $T_{\mathbf{A}}$ is equal to the rank of the matrix $\mathbf{A}$.
  $T_{\mathbf{A}}$ 的值域的维度等于矩阵 $\mathbf{A}$ 的秩。
- The image is a subspace of $\mathbb{R}^n$.
  值域是 $\mathbb{R}^n$ 的子空间。

## Kernel / 核

### Definition / 定义

The kernel (or null space) of a linear transformation $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$ is the set of all vectors $\mathbf{x} \in \mathbb{R}^m$ that are mapped to the zero vector in $\mathbb{R}^n$, i.e., $T_{\mathbf{A}}(\mathbf{x}) = \mathbf{A}\mathbf{x} = \mathbf{0}$.

线性变换 $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$ 的核（或零空间）是所有被映射到 $\mathbb{R}^n$ 中的零向量的 $\mathbb{R}^m$ 中的向量 $\mathbf{x}$ 的集合，即 $T_{\mathbf{A}}(\mathbf{x}) = \mathbf{A}\mathbf{x} = \mathbf{0}$。

$$
\mathrm{Ker}(T_{\mathbf{A}}) = \{\mathbf{x} \in \mathbb{R}^m \mid \mathbf{A}\mathbf{x} = \mathbf{0}\}
$$

### Properties / 性质

- The dimension of the kernel of $T_{\mathbf{A}}$ is called the nullity of $\mathbf{A}$.
  $T_{\mathbf{A}}$ 的核的维度称为 $\mathbf{A}$ 的零度。
- The kernel is a subspace of $\mathbb{R}^m$.
  核是 $\mathbb{R}^m$ 的子空间。

## Relationship between Image and Kernel / 值域和核的关系

### Rank-Nullity Theorem / 秩-零度定理

For a linear transformation $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$, the sum of the dimension of the image (rank) and the dimension of the kernel (nullity) is equal to the dimension of the domain $\mathbb{R}^m$:

对于线性变换 $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$，值域的维度（秩）和核的维度（零度）的和等于定义域 $\mathbb{R}^m$ 的维度：

$$
\mathrm{rank}(\mathbf{A}) + \mathrm{nullity}(\mathbf{A}) = m
$$
