class TrieNode:
    __slots__ = ("children", "user_ids")

    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.user_ids = []     # users whose username ends at this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, username, user_id):
        node = self.root
        for ch in username.lower():
            node = node.children.setdefault(ch, TrieNode())     # if ch already exists in children, return existing node. Otherwise, make a new node
        node.user_ids.append(user_id)

    def _collect(self, node, out):
        if node.user_ids:
            out.extend(node.user_ids)       # adds all user ids on current node
        for child in node.children.values():
            self._collect(child, out)

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix.lower():
            node = node.children.get(ch)
            if node is None:
                return []
        out = []
        self._collect(node, out)
        return out

    @classmethod                # static method
    def build(cls, graph):
        trie = cls()
        for user in graph.users.values():
            trie.insert(user.username, user.id)
        return trie
