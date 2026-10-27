from collections import Counter

def ucestalost(tekst):
    reci = tekst.lower().split()
    return Counter(reci)

if __name__ == "__main__":
    tekst = "Jabuka kruška jabuka šljiva kruška jabuka"
    counter = ucestalost(tekst)
    print(counter)
    print("Dve najčešće reči: ")
    print([rec for rec, broj in counter.most_common(2)])