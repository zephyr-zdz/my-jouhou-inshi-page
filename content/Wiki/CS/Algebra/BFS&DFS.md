# 广度/深度优先搜索 | Breadth-First Search (BFS) and Depth-First Search (DFS)

## 广度优先搜索 | Breadth-First Search (BFS)

### 定义 | Definition

广度优先搜索 (BFS) 是一种图搜索算法，从给定的起始节点开始，按层次顺序逐层访问图中的所有节点。

Breadth-First Search (BFS) is a graph traversal algorithm that starts from a given starting node and explores all its neighboring nodes at the present depth level before moving on to nodes at the next depth level.

### 工作原理 | Working Principle

1. **使用队列 | Using a Queue**
   - BFS 使用队列数据结构来跟踪当前层次的节点。
   - BFS uses a queue data structure to keep track of the current level of nodes.

2. **逐层访问 | Level-by-Level Exploration**
   - 从起始节点开始，将其标记为已访问并加入队列。
   - 从队列中取出一个节点，访问其所有未访问的邻居节点并将它们加入队列。
   - 重复直到队列为空。
   - Start from the initial node, mark it as visited and enqueue it.
   - Dequeue a node, visit all its unvisited neighboring nodes, and enqueue them.
   - Repeat until the queue is empty.

### 伪代码 | Pseudocode

```python
def bfs(graph, start):
    visited = set()  # 用于存储已访问的节点
    queue = []  # 队列初始化为空
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node)  # 访问节点

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
```

### 示例 | Example

假设有以下图结构：

Suppose we have the following graph structure:

```plaintext
    A
   / \
  B   C
 / \   \
D   E   F
```

调用 `bfs(graph, 'A')` 的结果是访问顺序：A, B, C, D, E, F。

### 应用 | Applications

- **最短路径搜索 | Shortest Path Search**
  - 在无权图中，BFS 可用于找到从起始节点到目标节点的最短路径。
  - In unweighted graphs, BFS can be used to find the shortest path from the start node to the target node.

- **分层遍历 | Layered Traversal**
  - 在需要按层次顺序访问节点的应用中，如社交网络分析。
  - In applications requiring layered traversal of nodes, such as social network analysis.

## 深度优先搜索 | Depth-First Search (DFS)

### 定义 | Definition

深度优先搜索 (DFS) 是一种图搜索算法，从给定的起始节点开始，沿着一个分支深入到图的尽头，然后回溯并继续搜索下一个分支。

Depth-First Search (DFS) is a graph traversal algorithm that starts from a given starting node and explores as far as possible along each branch before backtracking and exploring the next branch.

### 工作原理 | Working Principle

1. **使用栈 | Using a Stack**
   - DFS 通常使用栈数据结构来跟踪当前的路径节点。递归实现 DFS 也隐式地使用了调用栈。
   - DFS typically uses a stack data structure to keep track of the current path of nodes. Recursive implementations of DFS use the call stack implicitly.

2. **深入探索 | Deep Exploration**
   - 从起始节点开始，将其标记为已访问并压入栈。
   - 从栈中取出一个节点，访问其未访问的邻居节点并压入栈。
   - 重复直到栈为空。
   - Start from the initial node, mark it as visited and push it onto the stack.
   - Pop a node from the stack, visit its unvisited neighboring nodes, and push them onto the stack.
   - Repeat until the stack is empty.

### 伪代码 | Pseudocode

#### 递归实现 | Recursive Implementation

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)  # 访问节点

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
```

#### 迭代实现 | Iterative Implementation

```python
def dfs_iterative(graph, start):
    visited = set()  # 用于存储已访问的节点
    stack = []  # 栈初始化为空
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)  # 访问节点

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

### 示例 | Example

假设有以下图结构：

Suppose we have the following graph structure:

```plaintext
    A
   / \
  B   C
 / \   \
D   E   F
```

调用 `dfs_recursive(graph, 'A')` 或 `dfs_iterative(graph, 'A')` 的结果是访问顺序：A, B, D, E, C, F。

### 应用 | Applications

- **路径搜索 | Path Search**
  - 在迷宫或图中找到路径的应用中，如迷宫求解。
  - In applications requiring path finding in mazes or graphs, such as maze solving.

- **拓扑排序 | Topological Sorting**
  - 用于有向无环图 (DAG) 的拓扑排序。
  - Used for topological sorting of directed acyclic graphs (DAG).

- **连通分量 | Connected Components**
  - 在无向图中查找所有连通分量。
  - Finding all connected components in an undirected graph.

## BFS 和 DFS 的比较 | Comparison of BFS and DFS

| 特性 | BFS | DFS |
| ---- | --- | --- |
| 数据结构 | 队列 | 栈（或递归调用栈） |
| 访问顺序 | 按层次逐层访问 | 沿一个分支深入探索 |
| 最短路径 | 可以找到无权图中的最短路径 | 不保证最短路径 |
| 空间复杂度 | $O(V)$ | $O(V)$ |
| 时间复杂度 | $O(V + E)$ | $O(V + E)$ |
| 应用 | 最短路径、广度遍历 | 路径搜索、拓扑排序、连通分量 |

其中，$V$ 表示图中的顶点数量，$E$ 表示图中的边数量。

Where $V$ represents the number of vertices and $E$ represents the number of edges in the graph.

## 总结 | Summary

广度优先搜索 (BFS) 和 深度优先搜索 (DFS) 是两种基本的图搜索算法，各有优劣。理解它们的工作原理、实现方法及适用场景，可以有效地解决图中的各种问题。

Breadth-First Search (BFS) and Depth-First Search (DFS) are two fundamental graph traversal algorithms, each with its strengths and weaknesses. Understanding their principles, implementations, and application scenarios can effectively solve various problems in graphs.
