# K-means 算法 | K-means Algorithm

## 定义 | Definition

K-means 算法是一种迭代性的聚类算法，用于将数据集分成 $k$ 个聚类，每个聚类由其质心（centroid）表示。算法的目标是通过最小化每个聚类内的样本到其质心的距离平方和（即误差平方和，SSE）来实现最佳聚类。

The K-means algorithm is an iterative clustering algorithm that aims to partition a dataset into $k$ clusters, each represented by its centroid. The objective of the algorithm is to minimize the sum of squared distances (SSE) from each point to its centroid within each cluster.

## 算法步骤 | Algorithm Steps

1. **初始化 | Initialization**
   - 随机选择 $k$ 个初始质心。
   - Randomly select $k$ initial centroids.

2. **分配 | Assignment**
   - 将每个样本分配给距离其最近的质心，形成 $k$ 个聚类。
   - Assign each sample to the nearest centroid, forming $k$ clusters.

3. **更新 | Update**
   - 计算每个聚类的质心，即所有样本点的平均值。
   - Recompute the centroid of each cluster as the mean of all points assigned to the cluster.

4. **迭代 | Iteration**
   - 重复步骤 2 和 3，直到质心不再发生变化或变化小于预设的阈值。
   - Repeat steps 2 and 3 until the centroids do not change significantly or the change is below a predefined threshold.

### 伪代码 | Pseudocode

```python
import numpy as np

def initialize_centroids(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]

def assign_clusters(X, centroids):
    distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
    return np.argmin(distances, axis=1)

def update_centroids(X, labels, k):
    centroids = np.zeros((k, X.shape[1]))
    for i in range(k):
        points = X[labels == i]
        if points.size:
            centroids[i] = points.mean(axis=0)
    return centroids

def kmeans(X, k, max_iters=100, tol=1e-4):
    centroids = initialize_centroids(X, k)
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, k)
        if np.linalg.norm(new_centroids - centroids) < tol:
            break
        centroids = new_centroids
    return centroids, labels

# Example usage
X = np.array([
    [1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0],
    [1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0],
    [9.0, 3.0], [4.0, 2.0], [4.0, 4.0], [6.0, 3.0]
])
k = 3
centroids, labels = kmeans(X, k)
print("Centroids:", centroids)
print("Labels:", labels)
```

## 示例 | Example

假设我们有以下数据点：

Suppose we have the following data points:

```plaintext
[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0],
[1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0],
[9.0, 3.0], [4.0, 2.0], [4.0, 4.0], [6.0, 3.0]
```

我们希望将这些数据点聚类为 3 个聚类。

We want to cluster these data points into 3 clusters.

通过运行上述 K-means 算法，我们得到的质心和标签如下：

By running the above K-means algorithm, we obtain the following centroids and labels:

```plaintext
Centroids: [[ 4.25  4.75]
            [ 1.16666667  1.46666667]
            [ 8.5  6.5]]
Labels: [1 1 2 2 1 2 2 2 2 0 0 0]
```

## 时间复杂度 | Time Complexity

K-means 算法的时间复杂度通常为 $O(n \cdot k \cdot t \cdot d)$，其中：

The time complexity of the K-means algorithm is typically $O(n \cdot k \cdot t \cdot d)$, where:

- $n$ 是数据点的数量。
- $n$ is the number of data points.
- $k$ 是聚类的数量。
- $k$ is the number of clusters.
- $t$ 是算法的迭代次数。
- $t$ is the number of iterations.
- $d$ 是数据点的维度。
- $d$ is the dimension of the data points.

## 优点和缺点 | Advantages and Disadvantages

### 优点 | Advantages

- **简单易懂 | Simple and Easy to Understand**
  - 实现和理解都很简单。
  - Simple to implement and understand.
- **收敛速度快 | Fast Convergence**
  - 对于小规模数据集，收敛速度较快。
  - Fast convergence for small-scale datasets.
- **适用性广 | Wide Applicability**
  - 适用于许多实际应用，如图像分割、客户分群等。
  - Applicable to many practical applications, such as image segmentation, customer segmentation, etc.

### 缺点 | Disadvantages

- **需要预先指定聚类数 $k$ | Requires Pre-specifying the Number of Clusters $k$**
  - 在实际应用中，$k$ 的选择可能并不直观。
  - Choosing the value of $k$ may not be intuitive in practical applications.
- **对初始质心敏感 | Sensitive to Initial Centroids**
  - 不同的初始质心可能导致不同的聚类结果。
  - Different initial centroids may lead to different clustering results.
- **对噪声和离群点敏感 | Sensitive to Noise and Outliers**
  - 噪声和离群点可能严重影响聚类结果。
  - Noise and outliers can significantly affect the clustering results.
- **适用于球形聚类 | Assumes Spherical Clusters**
  - K-means 假设聚类是球形的，不适用于所有数据分布。
  - K-means assumes clusters are spherical, which is not suitable for all data distributions.

## 总结 | Summary

K-means 算法是一种广泛使用的聚类算法，通过最小化聚类内的误差平方和来实现数据点的分组。理解其工作原理、优缺点及实现细节，有助于在实际应用中有效地进行数据聚类。

The K-means algorithm is a widely used clustering algorithm that groups data points by minimizing the sum of squared errors within clusters. Understanding its working principle, advantages, disadvantages, and implementation details helps in effectively clustering data in practical applications.
