# Linear Transformation

A linear transformation is a mathematical function that maps vectors from one vector space to another, while preserving the operations of vector addition and scalar multiplication. Formally, a function $T: V \to W$ between two vector spaces $V$ and $W$ is called a linear transformation if for all vectors $\mathbf{u}, \mathbf{v} \in V$ and scalar $c \in \mathbb{R}$, the following properties hold:

1. **Additivity**: $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. **Homogeneity**: $T(c \mathbf{u}) = c T(\mathbf{u})$

### Representation of Linear Transformations

Linear transformations can be represented using matrices. If $V$ and $W$ are finite-dimensional vector spaces and $T: V \to W$ is a linear transformation, then there exists a matrix $A$ such that for any vector $\mathbf{v} \in V$,

$$
 T(\mathbf{v}) = A \mathbf{v} 
$$

Here, $A$ is called the matrix representation of the linear transformation $T$.

### Properties of Linear Transformations

1. **Composition**: The composition of two linear transformations is also a linear transformation. If $T_1: U \to V$ and $T_2: V \to W$ are linear transformations, then the composition $T_2 \circ T_1: U \to W$ is defined by $(T_2 \circ T_1)(\mathbf{u}) = T_2(T_1(\mathbf{u}))$ and is a linear transformation.

2. **Invertibility**: A linear transformation $T: V \to W$ is invertible if there exists a linear transformation $T^{-1}: W \to V$ such that $T^{-1}(T(\mathbf{v})) = \mathbf{v}$ for all $\mathbf{v} \in V$ and $T(T^{-1}(\mathbf{w})) = \mathbf{w}$ for all $\mathbf{w} \in W$. The matrix representation $A$ of an invertible linear transformation has an inverse matrix $A^{-1}$.

3. **Kernel and Image**: The kernel (or null space) of a linear transformation $T: V \to W$ is the set of all vectors in $V$ that map to the zero vector in $W$:

$$
 \text{ker}(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \} 
$$

The image (or range) of $T$ is the set of all vectors in $W$ that are images of vectors in $V$:

$$
 \text{im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} 
$$

4. **Rank-Nullity Theorem**: For a linear transformation $T: V \to W$, the dimension of $V$ (denoted as$\dim(V)$) is the sum of the dimensions of the kernel and the image:

$$
 \dim(V) = \text{rank}(T) + \text{nullity}(T) 
$$

where$\text{rank}(T) = \dim(\text{im}(T))$ and$\text{nullity}(T) = \dim(\text{ker}(T))$.

### Examples of Linear Transformations

1. **Identity Transformation**: The identity transformation $I: V \to V$ is defined by $I(\mathbf{v}) = \mathbf{v}$ for all $\mathbf{v} \in V$. Its matrix representation is the identity matrix.

2. **Rotation**: A rotation in the plane can be represented by a linear transformation. For an angle $\theta$, the rotation matrix is:

$$
 R(\theta) = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix} 
$$

3. **Scaling**: A scaling transformation changes the size of vectors. If $\alpha$ and $\beta$ are scaling factors in the $x$- and $y$-directions, respectively, the scaling matrix is:

$$
 S = \begin{bmatrix}
\alpha & 0 \\
0 & \beta
\end{bmatrix} 
$$

4. **Shear**: A shear transformation slants the shape of an object. A shear matrix along the $x$-axis with shear factor $k$ is:

$$
 H = \begin{bmatrix}
1 & k \\
0 & 1
\end{bmatrix} 
$$

### Determinant and Area Transformation

The determinant of the matrix $A$ representing a linear transformation $T$ provides information about the scaling factor of areas (in 2D) or volumes (in higher dimensions) under the transformation. Specifically, if $\mathbf{v}_1$ and $\mathbf{v}_2$ are vectors spanning a region in the plane, the area of the transformed region $T(\mathbf{v}_1)$ and $T(\mathbf{v}_2)$ is scaled by $|\det(A)|$.

### Quadratic Forms and Ellipses

A **quadratic form** is a polynomial of degree two in a number of variables. In the context of the given problem, the quadratic form $Q(x, y) = x^2 + xy + y^2$ plays a central role in defining the set$\Omega$. Quadratic forms can often be expressed in matrix notation as:

$$
 Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x} 
$$

where $\mathbf{x} = \begin{bmatrix} x \\ y \end{bmatrix}$ and $A$ is a symmetric matrix.

For the quadratic form $x^2 + xy + y^2$, the corresponding symmetric matrix $A$ is:

$$
 A = \begin{bmatrix}
1 & \frac{1}{2} \\
\frac{1}{2} & 1
\end{bmatrix} 
$$

### Ellipses and Their Transformations

Ellipses are the locus of points that satisfy a quadratic equation of the form:

$$
 ax^2 + bxy + cy^2 = 1
$$

For example ( [[IS_Math-2022-01]] ), the equation $x^2 + xy + y^2 = 1$ defines an ellipse centered at the origin. This specific ellipse is aligned with the coordinate axes, but has its shape influenced by the $xy$ cross-term, making it different from a standard axis-aligned ellipse.

When considering linear transformations of geometric shapes, such as transforming the unit circle to fit the boundary of an ellipse, we use a transformation matrix $\mathbf{X}$. For example, transforming the unit circle (defined by $x^2 + y^2 = 1$) to the ellipse given by $x^2 + xy + y^2 = 1$ involves finding a matrix $\mathbf{X}$ that maps the unit circle into the desired ellipse.

### Properties of Area under Transformation

One important property of linear transformations is their effect on areas. If a region in the plane is transformed by a linear transformation represented by matrix $\mathbf{X}$, the area of the transformed region is scaled by the absolute value of the determinant of $\mathbf{X}$.

For example, if we have a unit circle with area $\pi$, and we transform it using matrix $\mathbf{X}$ to obtain an ellipse, the area of the resulting ellipse can be calculated as:

$$
 \text{Area of Ellipse} = |\det(\mathbf{X})| \times \text{Area of Unit Circle} 
$$

Given that the area of the unit circle is$\pi$, the area of the ellipse would be:

$$
 \text{Area of Ellipse} = |\det(\mathbf{X})| \times \pi 
$$

### Application in the Given Problem

In the problem context, the set $\Omega$ is bounded by an ellipse defined by the quadratic inequality $x^2 + xy + y^2 < 1$. When we transform the unit circle into this ellipse using a specific transformation matrix $\mathbf{X}$, the determinant of this matrix provides a direct way to compute the area of $\Omega$.

Using the transformation matrix:

$$
 \mathbf{X} = \begin{bmatrix}
1 & \frac{1}{\sqrt{3}} \\
-1 & \frac{1}{\sqrt{3}}
\end{bmatrix} 
$$

we find that:

$$
 \det(\mathbf{X}) = \frac{2}{\sqrt{3}}
$$

Thus, the area of the ellipse (and hence the set $\Omega$) is:

$$
 \text{Area of } \Omega = \left| \frac{2}{\sqrt{3}} \right| \times \pi = \frac{2\pi}{\sqrt{3}} 
$$

This showcases how linear transformations, quadratic forms, and geometric properties such as area can be interconnected and applied to solve complex mathematical problems.

### Conclusion

Linear transformations are fundamental in linear algebra, providing a means to map vectors from one space to another while preserving the vector space structure. Understanding their properties, representations, and effects on geometric objects is crucial in various applications across mathematics and engineering.
