import heapq


class GraphArrays:
    def __init__(self, graph):
        self.nodes = list(graph.users.keys())          # index -> user id
        self.index = {node: i for i, node in enumerate(self.nodes)}     # user id -> index
        self.n = len(self.nodes)
        idx = self.index
        self.out_deg = [graph.out_degree(node) for node in self.nodes]  # count of every users 'follow out'
        self.followers_idx = [
            [idx[f] for f in graph.get_followers(node)] for node in self.nodes     # indexes in list of all user followers
        ]
        self.dangling = [i for i in range(self.n) if self.out_deg[i] == 0]  # users that follow no one


class PageRank:
    def __init__(self, graph, damping = 0.85, epsilon = 1e-6, max_iter = 100, arrays = None):
        self.graph = graph
        self.damping = damping  # ensures that the algorithm doesn't get stuck in a loop
        self.epsilon = epsilon      
        self.max_iter = max_iter
        self.arrays = arrays if arrays is not None else GraphArrays(graph)
        self.ranks = {}        # user id -> PageRank score
        self.iterations = 0    # iterations used by the last compute()

    def compute(self, initial = None):
        A = self.arrays
        n = A.n
        if n == 0:
            self.ranks = {}
            return self.ranks

        d = self.damping
        base = (1.0 - d) / n
        out_deg = A.out_deg
        followers = A.followers_idx
        dangling = A.dangling

        if initial:
            pr = [initial.get(node, 0.0) for node in A.nodes]
            total = sum(pr)
            pr = [x / total for x in pr] if total > 0 else [1.0 / n] * n
        else:
            pr = [1.0 / n] * n

        iterations = 0
        for _ in range(self.max_iter):
            iterations += 1

            dangling_mass = 0.0
            for i in dangling:
                dangling_mass += pr[i]
            redistributed = d * dangling_mass / n

            # Pre-divide each node's rank by its out-degree once per iteration.
            out_weight = [0.0] * n
            for i in range(n):
                od = out_deg[i]
                if od:
                    out_weight[i] = pr[i] / od

            new_pr = [0.0] * n
            diff = 0.0
            for i in range(n):
                s = 0.0
                for f in followers[i]:
                    s += out_weight[f]
                val = base + d * s + redistributed
                new_pr[i] = val
                diff += abs(val - pr[i])

            pr = new_pr
            if diff < self.epsilon:
                break

        self.iterations = iterations
        self.ranks = {A.nodes[i]: pr[i] for i in range(n)}
        return self.ranks

    def top(self, k):
        return heapq.nlargest(k, self.ranks.items(), key = lambda kv: kv[1])
