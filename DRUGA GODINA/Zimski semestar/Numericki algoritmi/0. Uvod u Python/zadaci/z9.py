def pokretni_prosek(niz, k):
    curr_sum = 0
    result = []

    for i in range(len(niz)):
        curr_sum += niz[i]

        if i >= k:
            curr_sum -= niz[i - k]

        if i >= k - 1:
            result.append(round(curr_sum / k, 2))

    return result


if __name__ == "__main__":
    print(pokretni_prosek([1, 2, 3, 4, 5, 6], 3))