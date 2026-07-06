import math

from text_processing import word_set, word_counts


def jaccard(bio_a, bio_b):
    return jaccard_prepared(word_set(bio_a), word_set(bio_b))


def cosine(bio_a, bio_b):
    ca, cb = word_counts(bio_a), word_counts(bio_b)
    return cosine_prepared(ca, vector_norm(ca), cb, vector_norm(cb))


def jaccard_prepared(set_a, set_b):
    if not set_a and not set_b:
        return 0.0
    union = len(set_a | set_b)      # number of total words of both bios
    if union == 0:
        return 0.0
    return len(set_a & set_b) / union   # jaccard formula


def vector_norm(counts):
    return math.sqrt(sum(v * v for v in counts.values()))   # length of biography vector


def cosine_prepared(counts_a, norm_a, counts_b, norm_b):
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    
    if len(counts_a) > len(counts_b):
        counts_a, counts_b = counts_b, counts_a

    dot = 0.0
    for word, ca in counts_a.items():
        cb = counts_b.get(word)
        if cb:
            dot += ca * cb          # scalar multiplication
    return dot / (norm_a * norm_b)
