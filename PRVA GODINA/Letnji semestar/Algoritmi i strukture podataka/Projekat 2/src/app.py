import time

from loader import load_social_graph
from models import User
from history import InteractionHistory
from inverted_index import InvertedIndex
from pagerank import GraphArrays, PageRank
from ppr import PersonalizedPageRank
from trie import Trie
from search import SearchEngine
from recommend import Recommender
from bfs import bfs_levels
from did_you_mean import did_you_mean
from text_processing import word_counts as _word_counts
from similarity import vector_norm


class SocialNetworkApp:
    def __init__(self, dataset_dir, damping = 0.85, epsilon = 1e-6):
        self.dataset_dir = dataset_dir
        self.damping = damping
        self.epsilon = epsilon

        self.graph = None
        self.history = InteractionHistory()
        self.username_to_id = {}
        self.all_usernames = []

        self.word_sets = {}          # id -> set of words      (Jaccard)
        self.word_counts = {}        # id -> Counter of words  (Cosine)
        self.word_norms = {}         # id -> vector norm        (Cosine)

        self.index = None            # inverted index
        self.trie = None
        self.arrays = None           # shared adjacency (Tasks 2, 7)
        self.pagerank = None
        self.ppr_engine = None
        self.search_engine = None
        self.recommender = None

        self.ranks_by_name = {}      # username -> PageRank

        self.timings = {}

    def build(self, verbose = False):
        t_total = time.perf_counter()

        t = time.perf_counter()
        self.graph = load_social_graph(self.dataset_dir, on_follow = self.history.record_follow)
        self.timings["graph_and_history"] = time.perf_counter() - t

        self._next_id = (max(self.graph.users) + 1) if self.graph.users else 1

        t = time.perf_counter()
        self.username_to_id = {u.username.lower(): u.id for u in self.graph.users.values()}
        self.all_usernames = [u.username for u in self.graph.users.values()]
        self.timings["username_index"] = time.perf_counter() - t

        t = time.perf_counter()
        self._build_text_structures()
        self.timings["text_structures"] = time.perf_counter() - t

        t = time.perf_counter()
        self.trie = Trie.build(self.graph)
        self.timings["trie"] = time.perf_counter() - t

        t = time.perf_counter()
        self.arrays = GraphArrays(self.graph)
        self.timings["graph_arrays"] = time.perf_counter() - t

        t = time.perf_counter()
        self.pagerank = PageRank(self.graph, self.damping, self.epsilon, arrays = self.arrays)
        self.pagerank.compute()
        self.timings["pagerank"] = time.perf_counter() - t

        self.ppr_engine = PersonalizedPageRank(self.graph, self.damping, self.epsilon, arrays = self.arrays)
        self.search_engine = SearchEngine(self.graph, self.index, self.pagerank.ranks)
        self.recommender = Recommender(self.graph, self.ppr_engine, self.word_sets, self.word_counts, self.word_norms)
        self._refresh_ranks_by_name()

        self.timings["total"] = time.perf_counter() - t_total
        if verbose:
            self.print_build_report()
        return self

    def _build_text_structures(self):
        index = InvertedIndex()
        word_sets, counts_map, norms = {}, {}, {}
        for user in self.graph.users.values():
            counts = _word_counts(user.bio)   # tokenize once
            words = set(counts.keys())
            counts_map[user.id] = counts
            word_sets[user.id] = words
            norms[user.id] = vector_norm(counts)
            index.add_words(user.id, words)
        self.index = index
        self.word_sets = word_sets
        self.word_counts = counts_map
        self.word_norms = norms

    def _refresh_ranks_by_name(self):
        ranks = self.pagerank.ranks
        self.ranks_by_name = {u.username: ranks.get(u.id, 0.0) for u in self.graph.users.values()}

    def get_user_by_id(self, user_id):
        return self.graph.get_user(user_id)

    def get_user_by_username(self, username):
        uid = self.username_to_id.get(username.strip().lower())
        return self.graph.get_user(uid) if uid is not None else None

    def did_you_mean(self, username, k = 5):
        return did_you_mean(username, self.all_usernames, k = k, ranks_by_name = self.ranks_by_name)

    def top_influencers(self, k = 10):
        return [(self.graph.get_user(uid), score) for uid, score in self.pagerank.top(k)]

    def search_username(self, query, k = 10):
        return [(self.graph.get_user(uid), rel) for uid, rel in self.search_engine.search_username(query, k)]

    def search_bio(self, query, k = 10):
        return [(self.graph.get_user(uid), matches) for uid, matches in self.search_engine.search_bio(query, k)]

    def interaction_history(self, user_id):
        following = [self.graph.get_user(uid) for uid in self.history.get_following_history(user_id)]
        followers = [self.graph.get_user(uid) for uid in self.history.get_followers_history(user_id)]
        return following, followers

    def autocomplete(self, prefix, k = 10):
        ranks = self.pagerank.ranks
        ids = self.trie.starts_with(prefix)
        ids.sort(key = lambda uid: ranks.get(uid, 0.0), reverse = True)
        return [(self.graph.get_user(uid), ranks.get(uid, 0.0)) for uid in ids[:k]]

    def bfs(self, user_id, max_level):
        levels = bfs_levels(self.graph, user_id, max_level)
        return {lvl: [self.graph.get_user(uid) for uid in ids] for lvl, ids in levels.items()}

    def recommend(self, user_id, alpha = 0.5, k = 10, measure = "jaccard"):
        return [(self.graph.get_user(uid), score) for uid, score in self.recommender.recommend(user_id, alpha, k, measure)]

    def add_user(self, username, bio):
        g = self.graph
        username = username.strip()
        bio = bio.strip()

        if username == "":
            return False, "Korisničko ime ne sme biti prazno."
        if username.lower() in self.username_to_id:
            return False, f"Korisničko ime '{username}' je već zauzeto."

        user_id = self._next_id
        self._next_id += 1

        user = User(user_id, username, bio)
        g.add_user(user)

        self.username_to_id[username.lower()] = user_id
        self.all_usernames.append(username)

        counts = _word_counts(bio)
        words = set(counts.keys())
        self.word_counts[user_id] = counts
        self.word_sets[user_id] = words
        self.word_norms[user_id] = vector_norm(counts)
        self.index.add_words(user_id, words)

        self.trie.insert(username, user_id)

        self._recompute_after_change()

        return True, f"Dodat korisnik {username} (id = {user_id})."

    def add_follow(self, from_id, to_id):
        g = self.graph
        if not g.has_user(from_id):
            return False, f"Korisnik sa id = {from_id} ne postoji."
        if not g.has_user(to_id):
            return False, f"Korisnik sa id = {to_id} ne postoji."
        if from_id == to_id:
            return False, "Korisnik ne može da prati samog sebe."
        if g.is_blocked_between(from_id, to_id):
            return False, "Veza nije dozvoljena: jedan od korisnika je blokirao drugog."
        if to_id in g.get_following(from_id):
            a, b = g.get_user(from_id).username, g.get_user(to_id).username
            return False, f"{a} već prati korisnika {b}."

        g.add_follow(from_id, to_id)
        self.history.record_follow(from_id, to_id)
        self._recompute_after_change()

        a, b = g.get_user(from_id).username, g.get_user(to_id).username
        return True, f"Dodato: {a} sada prati korisnika {b}."

    def _recompute_after_change(self):
        old_ranks = self.pagerank.ranks
        self.arrays = GraphArrays(self.graph)
        self.pagerank = PageRank(self.graph, self.damping, self.epsilon, arrays = self.arrays)
        self.pagerank.compute(initial = old_ranks)
        self.ppr_engine.arrays = self.arrays
        self.search_engine.ranks = self.pagerank.ranks
        self._refresh_ranks_by_name()

    def stats(self):
        return {
            "users": self.graph.num_users(),
            "follow_edges": self.graph.num_follow_edges(),
            "block_edges": self.graph.num_block_edges(),
            "index_words": self.index.num_words(),
            "pagerank_iterations": self.pagerank.iterations,
            "load_seconds": self.timings.get("total", 0.0),
        }

    def print_build_report(self):
        s = self.stats()
        print("Aplikacija je spremna.")
        print(f"  korisnika:           {s['users']}")
        print(f"  veza praćenja:       {s['follow_edges']}")
        print(f"  veza blokiranja:     {s['block_edges']}")
        print(f"  indeksiranih reci:   {s['index_words']}")
        print(f"  PageRank iteracija:  {s['pagerank_iterations']}")
        print(f"  vreme izgradnje:     {s['load_seconds']:.3f} s")
