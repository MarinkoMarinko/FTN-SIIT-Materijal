import re
from collections import Counter

# A token (word) contains lowercase letters, digits or underscores.
_TOKEN_RE = re.compile(r"[a-z0-9_]+")


def tokenize(text):
    return _TOKEN_RE.findall(text.lower())


def word_set(text):         # for Jaccard
    return set(tokenize(text))


def word_counts(text):      # for Cosine
    return Counter(tokenize(text))
