from collections import defaultdict

from text_processing import tokenize


class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)   # word -> set of user ids whose bio contains that word

    def add_user(self, user_id, bio):
        self.add_words(user_id, set(tokenize(bio)))

    def add_words(self, user_id, words):
        for word in words:
            self.index[word].add(user_id)

    def get(self, word):
        return self.index.get(word, set())

    def num_words(self):
        return len(self.index)

    @classmethod                            # static method
    def build(cls, graph):          
        idx = cls()
        for user in graph.users.values():
            idx.add_user(user.id, user.bio)
        return idx
