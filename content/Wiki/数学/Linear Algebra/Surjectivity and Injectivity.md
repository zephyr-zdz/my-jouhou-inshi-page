# Surjectivity and Injectivity of Linear Transformation

线性变换满射性和单射性

## Definition / 定义

Given a linear transformation $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$ defined by $T_{\mathbf{A}} (\mathbf{x}) = \mathbf{A} \mathbf{x}$, where $\mathbf{A}$ is an $n \times m$ matrix, we analyze the properties of surjectivity and injectivity.

给定由 $T_{\mathbf{A}} (\mathbf{x}) = \mathbf{A} \mathbf{x}$ 定义的线性变换 $T_{\mathbf{A}}: \mathbb{R}^m \to \mathbb{R}^n$，其中 $\mathbf{A}$ 是一个 $n \times m$ 矩阵，我们分析其满射性和单射性的性质。

## Surjectivity / 满射性

### Definition / 定义

A function $T_{\mathbf{A}}$ is surjective (onto) if for every $\mathbf{y} \in \mathbb{R}^n$, there exists at least one $\mathbf{x} \in \mathbb{R}^m$ such that $T_{\mathbf{A}} (\mathbf{x}) = \mathbf{y}$.

如果对每个 $\mathbf{y} \in \mathbb{R}^n$，至少存在一个 $\mathbf{x} \in \mathbb{R}^m$ 使得 $T_{\mathbf{A}} (\mathbf{x}) = \mathbf{y}$，则函数 $T_{\mathbf{A}}$ 是满射（到射）的。

### Conditions for Surjectivity / 满射性的条件

- $T_{\mathbf{A}}$ is surjective if and only if the matrix $\mathbf{A}$ has full row rank, i.e., $\mathrm{rank}(\mathbf{A}) = n$.
  当且仅当矩阵 $\mathbf{A}$ 满行秩，即 $\mathrm{rank}(\mathbf{A}) = n$ 时，$T_{\mathbf{A}}$ 是满射的。
- This implies that $\mathbf{A}$ has $n$ linearly independent rows.
  这意味着 $\mathbf{A}$ 有 $n$ 个线性无关的行。

### Example / 示例

Let $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$, which is a $3 \times 2$ matrix. Since $\mathbf{A}$ has rank 2, which is less than 3, $T_{\mathbf{A}}$ is not surjective.

令 $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$，这是一个 $3 \times 2$ 矩阵。由于 $\mathbf{A}$ 的秩是 2，小于 3，$T_{\mathbf{A}}$ 不是满射的。

## Injectivity / 单射性

### Definition / 定义

A function $T_{\mathbf{A}}$ is injective (one-to-one) if for every $\mathbf{x}_1, \mathbf{x}_2 \in \mathbb{R}^m$, $T_{\mathbf{A}} (\mathbf{x}_1) = T_{\mathbf{A}} (\mathbf{x}_2)$ implies $\mathbf{x}_1 = \mathbf{x}_2$.

如果对每个 $\mathbf{x}_1, \mathbf{x}_2 \in \mathbb{R}^m$，$T_{\mathbf{A}} (\mathbf{x}_1) = T_{\mathbf{A}} (\mathbf{x}_2)$ 蕴含 $\mathbf{x}_1 = \mathbf{x}_2$，则函数 $T_{\mathbf{A}}$ 是单射的。

### Conditions for Injectivity / 单射性的条件

- $T_{\mathbf{A}}$ is injective if and only if the matrix $\mathbf{A}$ has full column rank, i.e., $\mathrm{rank}(\mathbf{A}) = m$.
  当且仅当矩阵 $\mathbf{A}$ 满列秩，即 $\mathrm{rank}(\mathbf{A}) = m$ 时，$T_{\mathbf{A}}$ 是单射的。
- This implies that $\mathbf{A}$ has $m$ linearly independent columns.
  这意味着 $\mathbf{A}$ 有 $m$ 个线性无关的列。

### Example / 示例

Let $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, which is a $2 \times 2$ matrix. Since $\mathbf{A}$ has rank 1, which is less than 2, $T_{\mathbf{A}}$ is not injective.

令 $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$，这是一个 $2 \times 2$ 矩阵。由于 $\mathbf{A}$ 的秩是 1，小于 2，$T_{\mathbf{A}}$ 不是单射的。

## Combined Properties / 组合性质

### Bijectivity / 双射性

A function $T_{\mathbf{A}}$ is bijective (both injective and surjective) if $\mathbf{A}$ is a square matrix (i.e., $m = n$) and $\mathrm{rank}(\mathbf{A}) = m = n$.

如果 $\mathbf{A}$ 是一个方阵（即 $m = n$）且 $\mathrm{rank}(\mathbf{A}) = m = n$，则函数 $T_{\mathbf{A}}$ 是双射的。

### Example / 示例

Let $\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, which is a $2 \times 2$ identity matrix. Since $\mathbf{A}$ has rank 2 and is a square matrix, $T_{\mathbf{A}}$ is bijective.

令 $\mathbf{A} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$，这是一个 $2 \times 2$ 单位矩阵。由于 $\mathbf{A}$ 的秩是 2 且是一个方阵，$T_{\mathbf{A}}$ 是双射的。
