# 线性代数量的几何意义 | Geometric Meaning of Linear Algebra Quantities

## 向量的投影 | Projection of Vectors

### 向量在另一向量上的投影 | Projection of a Vector onto Another Vector

设有两个向量 $\mathbf{a}$ 和 $\mathbf{b}$，$\mathbf{a}$ 在 $\mathbf{b}$ 上的投影为：

$$
\mathrm{proj}_{\mathbf{b}}\mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b}
$$

其中 $\mathbf{a} \cdot \mathbf{b}$ 表示向量的点积。

The projection of vector $\mathbf{a}$ onto vector $\mathbf{b}$ is given by:

$$
\mathrm{proj}_{\mathbf{b}}\mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \mathbf{b}
$$

where $\mathbf{a} \cdot \mathbf{b}$ denotes the dot product of the vectors.

### 向量在某个平面上的投影 | Projection of a Vector onto a Plane

设 $\mathbf{n}$ 是平面法向量，$\mathbf{a}$ 在平面上的投影 $\mathbf{a}_{\text{proj}}$ 为：

$$
\mathbf{a}_{\text{proj}} = \mathbf{a} - \mathrm{proj}_{\mathbf{n}}\mathbf{a} = \mathbf{a} - \frac{\mathbf{a} \cdot \mathbf{n}}{\mathbf{n} \cdot \mathbf{n}} \mathbf{n}
$$

Let $\mathbf{n}$ be the normal vector to the plane. The projection of vector $\mathbf{a}$ onto the plane, denoted by $\mathbf{a}_{\text{proj}}$, is:

$$
\mathbf{a}_{\text{proj}} = \mathbf{a} - \mathrm{proj}_{\mathbf{n}}\mathbf{a} = \mathbf{a} - \frac{\mathbf{a} \cdot \mathbf{n}}{\mathbf{n} \cdot \mathbf{n}} \mathbf{n}
$$

## 点线面之间的距离 | Distances Between Points, Lines, and Planes

### 点到直线的距离 | Distance from a Point to a Line

点 $\mathbf{P}_0$ 到直线 $\mathbf{L}: \mathbf{r} = \mathbf{r}_0 + t\mathbf{d}$ 的距离为：

$$
\text{dist}(\mathbf{P}_0, \mathbf{L}) = \frac{\|\mathbf{d} \times (\mathbf{P}_0 - \mathbf{r}_0)\|}{\|\mathbf{d}\|}
$$

The distance from point $\mathbf{P}_0$ to the line $\mathbf{L}: \mathbf{r} = \mathbf{r}_0 + t\mathbf{d}$ is:

$$
\text{dist}(\mathbf{P}_0, \mathbf{L}) = \frac{\|\mathbf{d} \times (\mathbf{P}_0 - \mathbf{r}_0)\|}{\|\mathbf{d}\|}
$$

### 点到平面的距离 | Distance from a Point to a Plane

点 $\mathbf{P}_0$ 到平面 $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ 的距离为：

$$
\text{dist}(\mathbf{P}_0, \text{Plane}) = \frac{|\mathbf{n} \cdot (\mathbf{P}_0 - \mathbf{r}_0)|}{\|\mathbf{n}\|}
$$

The distance from point $\mathbf{P}_0$ to the plane $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ is:

$$
\text{dist}(\mathbf{P}_0, \text{Plane}) = \frac{|\mathbf{n} \cdot (\mathbf{P}_0 - \mathbf{r}_0)|}{\|\mathbf{n}\|}
$$

### 两直线之间的距离 | Distance Between Two Skew Lines

对于不相交的直线 $\mathbf{L}_1: \mathbf{r} = \mathbf{r}_1 + t\mathbf{d}_1$ 和 $\mathbf{L}_2: \mathbf{r} = \mathbf{r}_2 + s\mathbf{d}_2$，它们之间的距离为：

$$
\text{dist}(\mathbf{L}_1, \mathbf{L}_2) = \frac{|(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|}
$$

For two skew lines $\mathbf{L}_1: \mathbf{r} = \mathbf{r}_1 + t\mathbf{d}_1$ and $\mathbf{L}_2: \mathbf{r} = \mathbf{r}_2 + s\mathbf{d}_2$, the distance between them is:

$$
\text{dist}(\mathbf{L}_1, \mathbf{L}_2) = \frac{|(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{d}_1 \times \mathbf{d}_2)|}{\|\mathbf{d}_1 \times \mathbf{d}_2\|}
$$

## 面积与体积 | Area and Volume

### 三角形的面积 | Area of a Triangle

给定三角形的顶点 $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$，三角形的面积 $\mathrm{Area}$ 为：

$$
\mathrm{Area} = \frac{1}{2} \|\mathbf{AB} \times \mathbf{AC}\|
$$

其中，$\mathbf{AB}$ 和 $\mathbf{AC}$ 分别是 $\mathbf{A}$ 到 $\mathbf{B}$ 和 $\mathbf{A}$ 到 $\mathbf{C}$ 的向量。

Given the vertices $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{C}$ of a triangle, the area $\mathrm{Area}$ is:

$$
\mathrm{Area} = \frac{1}{2} \|\mathbf{AB} \times \mathbf{AC}\|
$$

where $\mathbf{AB}$ and $\mathbf{AC}$ are vectors from $\mathbf{A}$ to $\mathbf{B}$ and $\mathbf{A}$ to $\mathbf{C}$, respectively.

### 四面体的体积 | Volume of a Tetrahedron

给定四面体的四个顶点 $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$，体积 $\mathrm{Volume}$ 为：

$$
\mathrm{Volume} = \frac{1}{6} |(\mathbf{AB} \times \mathbf{AC}) \cdot \mathbf{AD}|
$$

其中，$\mathbf{AB}$, $\mathbf{AC}$, $\mathbf{AD}$ 是从 $\mathbf{A}$ 出发到 $\mathbf{B}$, $\mathbf{C}$ 和 $\mathbf{D}$ 的向量。

Given the vertices $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, and $\mathbf{D}$ of a tetrahedron, the volume $\mathrm{Volume}$ is:

$$
\mathrm{Volume} = \frac{1}{6} |(\mathbf{AB} \times \mathbf{AC}) \cdot \mathbf{AD}|
$$

where $\mathbf{AB}$, $\mathbf{AC}$, and $\mathbf{AD}$ are vectors from $\mathbf{A}$ to $\mathbf{B}$, $\mathbf{C}$, and $\mathbf{D}$, respectively.

## 线性变换的几何意义 | Geometric Meaning of Linear Transformations

### 线性变换对面积的影响 | Effect of Linear Transformation on Area

对于线性变换 $\mathbf{T}$，如果 $\mathbf{T}$ 映射平面上三角形的三个顶点 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$，则变换后三角形的面积 $\mathrm{Area}'$ 为原面积 $\mathrm{Area}$ 的 $\det(\mathbf{T})$ 倍：

$$
\mathrm{Area}' = |\det(\mathbf{T})| \cdot \mathrm{Area}
$$

For a linear transformation $\mathbf{T}$, if $\mathbf{T}$ maps the three vertices $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ of a triangle in the plane, the area $\mathrm{Area}'$ of the transformed triangle is $\det(\mathbf{T})$ times the original area $\mathrm{Area}$:

$$
\mathrm{Area}' = |\det(\mathbf{T})| \cdot \mathrm{Area}
$$

### 线性变换对体积的影响 | Effect of Linear Transformation on Volume

对于线性变换 $\mathbf{T}$，如果

 $\mathbf{T}$ 映射三维空间中四面体的四个顶点 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4$，则变换后四面体的体积 $\mathrm{Volume}'$ 为原体积 $\mathrm{Volume}$ 的 $\det(\mathbf{T})$ 倍：

$$
\mathrm{Volume}' = |\det(\mathbf{T})| \cdot \mathrm{Volume}
$$

For a linear transformation $\mathbf{T}$, if $\mathbf{T}$ maps the four vertices $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3, \mathbf{v}_4$ of a tetrahedron in three-dimensional space, the volume $\mathrm{Volume}'$ of the transformed tetrahedron is $\det(\mathbf{T})$ times the original volume $\mathrm{Volume}$:

$$
\mathrm{Volume}' = |\det(\mathbf{T})| \cdot \mathrm{Volume}
$$
