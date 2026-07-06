from pagerank import GraphArrays


class PersonalizedPageRank:
    def __init__(self, graph, damping = 0.85, epsilon = 1e-6, max_iter = 100, arrays = None):
        self.graph = graph
        self.damping = damping
        self.epsilon = epsilon
        self.max_iter = max_iter
        self.arrays = arrays if arrays is not None else GraphArrays(graph)
        self.iterations = 0

    def compute(self, source_id):
        A = self.arrays
        n = A.n
        if n == 0 or source_id not in A.index:
            return {}

        d = self.damping
        out_deg = A.out_deg
        followers = A.followers_idx
        dangling = A.dangling
        src = A.index[source_id]
        restart = 1.0 - d  # teleport probability;

        pr = [0.0] * n
        pr[src] = 1.0

        iterations = 0
        for _ in range(self.max_iter):
            iterations += 1

            dangling_mass = 0.0
            for i in dangling:
                dangling_mass += pr[i]

            out_weight = [0.0] * n
            for i in range(n):
                od = out_deg[i]
                if od:
                    out_weight[i] = pr[i] / od

            new_pr = [0.0] * n
            for i in range(n):
                s = 0.0
                for f in followers[i]:
                    s += out_weight[f]
                new_pr[i] = d * s

            new_pr[src] += restart + d * dangling_mass

            diff = 0.0
            for i in range(n):
                diff += abs(new_pr[i] - pr[i])

            pr = new_pr
            if diff < self.epsilon:
                break

        self.iterations = iterations
        return {A.nodes[i]: pr[i] for i in range(n)}
