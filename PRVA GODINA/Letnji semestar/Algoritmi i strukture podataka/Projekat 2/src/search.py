import heapq

from text_processing import tokenize


class SearchEngine:
    def __init__(self, graph, inverted_index, ranks):
        self.graph = graph
        self.index = inverted_index
        self.ranks = ranks  # dict user_id -> PageRank score

    def search_username(self, query, k = 10):
        q = query.strip().lower()
        if not q:
            return []
        results = []
        for user in self.graph.users.values():
            name = user.username.lower()
            if q in name:
                if name == q:
                    relevance = 3       # exact match
                elif name.startswith(q):
                    relevance = 2       # prefix match
                else:
                    relevance = 1       # substring match
                results.append((user.id, relevance))
        return self._top(results, k)

    def search_bio(self, query, k = 10):
        words = set(tokenize(query))
        if not words:
            return []
        match_count = {}
        for word in words:
            for uid in self.index.get(word):
                match_count[uid] = match_count.get(uid, 0) + 1
        return self._top(list(match_count.items()), k)

    def _top(self, scored, k):
        ranks = self.ranks
        return heapq.nlargest(k, scored, key = lambda r: (r[1], ranks.get(r[0], 0.0)))
