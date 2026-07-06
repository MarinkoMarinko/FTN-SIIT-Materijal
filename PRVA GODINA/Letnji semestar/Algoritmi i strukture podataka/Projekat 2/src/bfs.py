def bfs_levels(graph, start_id, max_level):
    if not graph.has_user(start_id) or max_level < 1:
        return {}

    visited = {start_id}        # already seen users
    levels = {}                 # result
    frontier = [start_id]       # users that are currently being read
    level = 0

    while frontier and level < max_level:
        level += 1
        next_frontier = []
        for node in frontier:
            for neighbor in graph.get_following(node):
                if neighbor not in visited:     # prevents infinite loop (happens if users follow eachother)
                    visited.add(neighbor)
                    next_frontier.append(neighbor)
        if next_frontier:
            levels[level] = next_frontier
        frontier = next_frontier

    return levels
