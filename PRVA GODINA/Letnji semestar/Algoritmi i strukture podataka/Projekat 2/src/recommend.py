import heapq

from similarity import jaccard_prepared, cosine_prepared


class Recommender:
    def __init__(self, graph, ppr_engine, word_sets, word_counts, word_norms):
        self.graph = graph
        self.ppr_engine = ppr_engine
        self.word_sets = word_sets      # set of words in user biography for Jaccard
        self.word_counts = word_counts  # number of every word appearance in user biography for Cosine
        self.word_norms = word_norms    # calculated vector for Cosine

    def recommend(self, user_id, alpha = 0.5, k = 10, measure = "jaccard"):
        g = self.graph
        if not g.has_user(user_id):
            return []

        ppr = self.ppr_engine.compute(user_id)

        following = g.get_following(user_id)
        blocked = g.blocked.get(user_id, set())
        blocked_by = g.blocked_by.get(user_id, set())
        excluded = {user_id} | following | blocked | blocked_by     # users that won't be recommended

        candidates = [cid for cid in g.users if cid not in excluded]
        if not candidates:
            return []

        max_ppr = max((ppr.get(c, 0.0) for c in candidates), default = 0.0)
        if max_ppr <= 0.0:
            max_ppr = 1.0

        src_set = self.word_sets.get(user_id, set())
        src_counts = self.word_counts.get(user_id, {})
        src_norm = self.word_norms.get(user_id, 0.0)

        scored = []
        for cid in candidates:
            ppr_norm = ppr.get(cid, 0.0) / max_ppr
            if measure == "cosine":
                sim = cosine_prepared(src_counts, src_norm,
                                      self.word_counts.get(cid, {}),
                                      self.word_norms.get(cid, 0.0))
            else:
                sim = jaccard_prepared(src_set, self.word_sets.get(cid, set()))

            score = alpha * ppr_norm + (1.0 - alpha) * sim
            if score > 0.0:
                scored.append((cid, score))

        return heapq.nlargest(k, scored, key = lambda x: x[1])
