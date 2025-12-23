def dfs_helper(adj, src, visited, opt):
    visited[src] = True
    opt.append(src)

    # visit the ngb using dfs
    for ngb in adj[src]:
        if not visited[ngb]:
            dfs_helper(adj, ngb, visited, opt)


def dfs(adj, src):
    n = len(adj)
    visited = [False] * n
    opt = []
    dfs_helper(adj, src, visited, opt)
    return opt


# Driver code
adj = [[], [0, 5, 2], [1, 3], [2, 4], [3, 5], [1, 4]]  # Adjacency list

res = dfs(adj, 2)   # Perform DFS
print(" ".join(map(str, res)))

