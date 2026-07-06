# Performanse

Vremena su merena sa Python 3.12.3, koristeći samo standardnu biblioteku.
Merenja vremena zavise od mašine i trenutnog opterećenja; u nastavku je relativna
cena svake funkcionalnosti. PageRank koristi damping 0.85 i epsilon 1e-6.

## Veličine skupova podataka

| Skup   | Korisnika | Veza praćenja | Veza blokiranja | Indeksiranih reči |
| ------ | --------- | ------------- | --------------- | ----------------- |
| small  | 1.000     | 80.693        | 20              | 5.445             |
| medium | 10.000    | 354.503       | 200             | 39.363            |
| full   | 81.306    | 1.768.135     | 1.626           | 148.036           |

## Vreme izgradnje pri pokretanju (učitavanje + sve strukture, jednom)

| Skup   | Vreme izgradnje | PageRank iteracija |
| ------ | --------------- | ------------------ |
| small  | ~0,19 s         | 31                 |
| medium | ~1,3 s          | 50                 |
| full   | ~14,0 s         | 58                 |

Razlaganje izgradnje za **full** (u sekundama):

| Korak                        | Vreme    |
| ---------------------------- | -------- |
| graf + istorija interakcija  | 3,4      |
| indeks korisničkih imena     | 0,0      |
| bio vektori + inverted index | 1,9      |
| trie                         | 2,7      |
| nizovi grafa (susedstvo)     | 1,2      |
| PageRank                     | 4,9      |
| **ukupno**                   | **14,1** |

Najteži koraci pri pokretanju su računanje PageRank-a nad 1,77M veza,
učitavanje/parsiranje grafa i izgradnja trie-a. Sve se gradi jednom; nijedna
struktura se ne gradi ponovo po pojedinačnoj operaciji u meniju.

## Vreme operacija nad full skupom

| Operacija                             | Vreme   | Napomena                                       |
| ------------------------------------- | ------- | ---------------------------------------------- |
| Najuticajniji korisnici               | <0,01 s | heap nad unapred izračunatim PageRank-om       |
| Pretraga po korisničkom imenu         | <0,01 s | prolaz kroz korisnička imena                   |
| Pretraga po biografiji                | <0,01 s | pretraga preko inverted index-a                |
| Autocomplete (prefiks)                | <0,01 s | obilazak trie-a + sortiranje po PageRank-u     |
| BFS do nivoa 3                        | ~0,03 s | najaktivniji korisnik (~52.000 dosegnutih)     |
| Da li ste mislili                     | ~0,68 s | Levenštajn sa filterom po dužini               |
| Preporuka (hibridna, PPR)             | ~5,1 s  | Personalized PageRank nad 1,77M veza           |
| Dodaj vezu + warm-start PageRank      | ~1,1 s  | ponovna izgradnja susedstva + 6 warm iteracija |
| Dodaj korisnika + warm-start PageRank | ~0,8 s  | ponovna izgradnja susedstva + 3 warm iteracije |

## Napomene

- **Medium je interaktivan:** izgradnja ~1,3 s, a najskuplja operacija,
  hibridna preporuka, traje ~0,48 s.
- **Najskuplja operacija nad full skupom** je hibridna preporuka, jer pokreće
  Personalized PageRank iz izabranog korisnika nad svih 1,77M veza pri svakom
  pozivu. To je bio očekivani rizik za full skup; nad manjim skupovima je brzo.
- **Warm start jasno pomaže:** pun PageRank od nule traži ~58 iteracija, dok
  ponovno računanje nakon jedne nove veze (uz korišćenje prethodnih vrednosti)
  konvergira za 6. Dodavanje novog (izolovanog) korisnika gotovo da ne menja
  vrednosti, pa konvergira u svega 3 iteracije.
- Deljeni nizovi susedstva (`GraphArrays`) grade se jednom i koriste ih i
  PageRank i Personalized PageRank, pa preporuka ne gradi ponovo reprezentaciju
  grafa.
