import os
import sys
import time

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_BASE_DIR, "src"))

from app import SocialNetworkApp


def timed(label, func, repeats = 1):
    result = func()

    t = time.perf_counter()
    for _ in range(repeats):
        result = func()
    elapsed = (time.perf_counter() - t) / repeats

    if elapsed < 1e-3:
        print(f"  {label:<38} {elapsed * 1e6:8.1f} us  (prosek od {repeats})")
    elif elapsed < 1.0:
        print(f"  {label:<38} {elapsed * 1e3:8.2f} ms  (prosek od {repeats})")
    else:
        print(f"  {label:<38} {elapsed:8.3f} s")
    return result


def main():
    dataset = sys.argv[1] if len(sys.argv) > 1 else "small"
    dataset_dir = os.path.join(_BASE_DIR, "data", dataset)

    BFS_USER = 1                 
    BFS_LEVEL = 3
    REC_USER = 1                 # user for recommend
    REC_ALPHA = 0.6
    REC_MEASURE = "jaccard"
    USERNAME_QUERY = "reece"     
    BIO_QUERY = "music love"   
    AUTOCOMPLETE_PREFIX = "ree"
    TYPO_NAME = "reeceee"

    FOLLOW_FROM = 1
    FOLLOW_TO = 818

    print(f"=== Skup podataka: {dataset} ({dataset_dir}) ===\n")

    print("Izgradnja (build):")
    t = time.perf_counter()
    app = SocialNetworkApp(dataset_dir)
    app.build(verbose = False)
    build_total = time.perf_counter() - t

    for key in ("graph_and_history", "username_index", "text_structures", "trie", "graph_arrays", "pagerank"):
        sec = app.timings.get(key, 0.0)
        print(f"  {key:<38} {sec:8.3f} s")
    print(f"  {'UKUPNO':<38} {app.timings.get('total', build_total):8.3f} s")
    print(f"  PageRank iteracija (od nule):             {app.pagerank.iterations}")
    print()

    print("Operacije (read-only):")
    timed("Najuticajniji (top 10)",
          lambda: app.top_influencers(10), repeats = 50)
    timed("Pretraga po imenu",
          lambda: app.search_username(USERNAME_QUERY, 10), repeats = 50)
    timed("Pretraga po biografiji",
          lambda: app.search_bio(BIO_QUERY, 10), repeats = 50)
    timed("Autocomplete (prefiks)",
          lambda: app.autocomplete(AUTOCOMPLETE_PREFIX, 10), repeats = 50)
    timed("Did you mean",
          lambda: app.did_you_mean(TYPO_NAME), repeats = 10)
    timed(f"BFS do nivoa {BFS_LEVEL}",
          lambda: app.bfs(BFS_USER, BFS_LEVEL), repeats = 5)
    timed("Preporuka (hibridna, PPR)",
          lambda: app.recommend(REC_USER, REC_ALPHA, 10, REC_MEASURE), repeats = 1)
    print()

    print("Operacije sa izmenom grafa (warm start) - mere se jednom:")

    t = time.perf_counter()
    ok, msg = app.add_follow(FOLLOW_FROM, FOLLOW_TO)
    dt = time.perf_counter() - t
    iteration = app.pagerank.iterations
    print(f"  add_follow + warm PageRank   {dt:.3f} s   (iteracija: {iteration}) -> {msg}")

    t = time.perf_counter()
    ok, msg = app.add_user("novi_korisnik", "machine learning python developer")
    dt = time.perf_counter() - t
    iteration = app.pagerank.iterations
    print(f"  add_user + warm PageRank     {dt:.3f} s   (iteracija: {iteration}) -> {msg}")


if __name__ == "__main__":
    main()