class User:
    __slots__ = ("id", "username", "bio")

    def __init__(self, user_id, username, bio):
        self.id = user_id
        self.username = username 
        self.bio = bio

    def __repr__(self):         # similar to __str__()
        return f"User(id={self.id}, username={self.username!r})"


class SocialGraph:
    def __init__(self):
        self.users = {}
        self.following = {}
        self.followers = {}
        self.blocked = {}
        self.blocked_by = {}

    def add_user(self, user):
        self.users[user.id] = user
        self._ensure_node(user.id)

    def _ensure_node(self, user_id):
        if user_id not in self.following:
            self.following[user_id] = set()
            self.followers[user_id] = set()
            self.blocked[user_id] = set()
            self.blocked_by[user_id] = set()

    def add_follow(self, from_id, to_id):
        # from-id -> to_id
        if from_id == to_id:
            return
        
        self._ensure_node(from_id)
        self._ensure_node(to_id)
        self.following[from_id].add(to_id)
        self.followers[to_id].add(from_id)

    def add_block(self, blocker_id, blocked_id):
        if blocker_id == blocked_id:
            return      # user cannot block himself / herself
        
        self._ensure_node(blocker_id)
        self._ensure_node(blocked_id)
        self.blocked[blocker_id].add(blocked_id)
        self.blocked_by[blocked_id].add(blocker_id)

    def has_user(self, user_id):
        return user_id in self.users

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_following(self, user_id):
        return self.following.get(user_id, set())

    def get_followers(self, user_id):
        return self.followers.get(user_id, set())

    def out_degree(self, user_id):
        return len(self.following.get(user_id, ()))

    def in_degree(self, user_id):
        return len(self.followers.get(user_id, ()))

    def is_blocked_between(self, a_id, b_id):
        return (b_id in self.blocked.get(a_id, ())
                or a_id in self.blocked.get(b_id, ()))

    def num_users(self):
        return len(self.users)

    def num_follow_edges(self):     # counts all follows
        return sum(len(s) for s in self.following.values())

    def num_block_edges(self):      # counts all 'blockings'
        return sum(len(s) for s in self.blocked.values())
