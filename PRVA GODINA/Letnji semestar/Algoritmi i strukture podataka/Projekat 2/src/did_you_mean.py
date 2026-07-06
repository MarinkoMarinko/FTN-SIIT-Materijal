def levenshtein(a, b):      # calculates the distance between two words (change, add, delete)
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    previous = list(range(len(b) + 1))      # previous row
    for i, ca in enumerate(a, start = 1):
        current = [i]
        for j, cb in enumerate(b, start = 1):
            insert_cost = current[j - 1] + 1
            delete_cost = previous[j] + 1
            replace_cost = previous[j - 1] + (ca != cb)
            current.append(min(insert_cost, delete_cost, replace_cost))
        previous = current
    return previous[-1]


def did_you_mean(query, usernames, k = 5, ranks_by_name = None):     # recommends similar users
    q = query.strip().lower()
    if not q:
        return []

    qlen = len(q)
    window = max(2, qlen // 2)  # only compare names of similar length

    scored = []
    for name in usernames:
        lname = name.lower()
        if abs(len(lname) - qlen) > window:
            continue
        dist = levenshtein(q, lname)
        rank = ranks_by_name.get(name, 0.0) if ranks_by_name else 0.0
        scored.append((dist, -rank, name))  # sort by distance ascending, then by PageRank descending

    scored.sort()
    return [name for _, _, name in scored[:k]]
