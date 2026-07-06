from collections import defaultdict     # default dict - smarter dictionary, makes a default value if key doesn't exist


class InteractionHistory:
    def __init__(self):
        self.followed = defaultdict(list)      
        self.followed_by = defaultdict(list)

    def record_follow(self, from_id, to_id):
        self.followed[from_id].append(to_id)
        self.followed_by[to_id].append(from_id)

    def get_following_history(self, user_id):
        return self.followed.get(user_id, [])

    def get_followers_history(self, user_id):
        return self.followed_by.get(user_id, [])
