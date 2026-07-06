import os

from models import User, SocialGraph


def _iter_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield line


def load_users(path, graph):
    skipped = 0
    for line in _iter_lines(path):
        parts = line.split("|", 2)
        if len(parts) != 3:
            skipped += 1
            continue
        raw_id, username, bio = parts
        try:
            user_id = int(raw_id)
        except ValueError:
            skipped += 1
            continue
        graph.add_user(User(user_id, username, bio))
    return skipped


def load_connections(path, graph, on_follow = None):
    skipped = 0
    for line in _iter_lines(path):
        parts = line.split("|")
        if len(parts) != 2:
            skipped += 1
            continue
        try:
            from_id, to_id = int(parts[0]), int(parts[1])
        except ValueError:
            skipped += 1
            continue
        if from_id == to_id:
            continue            # ignores self follow
        graph.add_follow(from_id, to_id)
        if on_follow is not None:
            on_follow(from_id, to_id)       # records the follow in history
    return skipped


def load_blocked(path, graph):
    skipped = 0
    for line in _iter_lines(path):
        parts = line.split("|")
        if len(parts) != 2:
            skipped += 1
            continue
        try:
            blocker_id, blocked_id = int(parts[0]), int(parts[1])
        except ValueError:
            skipped += 1
            continue
        graph.add_block(blocker_id, blocked_id)
    return skipped


def load_social_graph(dataset_dir, on_follow = None):
    users_path = os.path.join(dataset_dir, "users.txt")
    connections_path = os.path.join(dataset_dir, "connections.txt")
    blocked_path = os.path.join(dataset_dir, "blocked.txt")

    for path in (users_path, connections_path, blocked_path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Missing data file: {path}")

    graph = SocialGraph()
    load_users(users_path, graph)
    load_connections(connections_path, graph, on_follow = on_follow)
    load_blocked(blocked_path, graph)
    return graph
