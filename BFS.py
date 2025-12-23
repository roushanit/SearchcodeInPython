from collections import deque

# Function to find BFS of Graph from given source s
def bfs(adj, src):
    n = len(adj)
    res = []

    q = deque()
    visited = [False] * n

    # src to queue
    visited[src] = True
    q.append(src)

    # main logic start
    while q:
        curr = q.popleft()
        res.append(curr)

        # check neighbors
        for ngb in adj[curr]:
            if not visited[ngb]:
                visited[ngb] = 1
                q.append(ngb)

    return res


# create the adjacency list
adj = [[1, 2], [0, 2, 3], [0, 4], [1, 4], [2, 3]]

ans = bfs(adj, 0)  # 0 1 2 3 4
for i in ans:
    print(i, end=" ")

