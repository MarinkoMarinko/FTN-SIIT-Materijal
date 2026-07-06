# Simulacija društvene mreže (ASP Projekat 2)

Konzolna aplikacija koja simulira deo društvene mreže izgrađene nad
**usmerenim grafom praćenja**. Aplikacija jednom učita priloženi skup
podataka, izgradi sve strukture u memoriji i kroz tekstualni meni nudi
pretragu, rangiranje uticaja (PageRank), autocomplete, obilazak mreže (BFS) i
hibridne preporuke.

## Pokretanje

Jezik: **Python 3.12.3+** (bez dodatnih paketa).
Prilikom **PRVOG** pokretanja programa, dodati podatke sa linka (nalazi se u folderu info u fajlu 'link za podatke.txt') u folder. Folder preimenovati u 'data' i postaviti ga u istom nivou sa fajlom 'main.py'. Nakon toga možete pokretati program na klasičan način, kucanjem komande _python main.py_ ili _python3 main.py_ u terminalu.

Pri pokretanju, program učita izabrani skup podataka, izgradi sve strukture i
ispiše kratak izveštaj (broj korisnika, veza, indeksiranih reči, broj PageRank
iteracija i vreme izgradnje). Zatim se prikazuje meni.

## Ulazni fajlovi

Svaki folder skupa podataka (`data/small`, `data/medium`, `data/full`)
sadrži tri tekstualna fajla razdvojena znakom `|`:

| Fajl              | Format                   | Značenje                              |
| ----------------- | ------------------------ | ------------------------------------- |
| `users.txt`       | `id\|username\|bio`      | jedan korisnik po liniji;             |
| `connections.txt` | `from_id\|to_id`         | `from_id` prati `to_id` (usmereno)    |
| `blocked.txt`     | `blocker_id\|blocked_id` | `blocker_id` je blokirao `blocked_id` |

## Opcije menija

```
 1) Pretraga po korisničkom imenu     (Zad 3)
 2) Pretraga po biografiji            (Zad 3)
 3) Najuticajniji korisnici           (Zad 2)
 4) Dodaj novog korisnika             (Zad 1 i 2)
 5) Dodaj vezu praćenja               (Zad 2 i 10)
 6) Istorija interakcija korisnika    (Zad 4)
 7) Autocomplete korisničkog imena    (Zad 6)
 8) Obilazak mreže (BFS po nivoima)   (Zad 8)
 9) Preporuka korisnika (hibridna)    (Zad 7 i 10)
 0) Izlaz                             (Zad 5)
```

## Implementirane funkcionalnosti

- **Zad 1 – Graf:** klase `User` i `SocialGraph` sa hash mapama za brzo
  pronalaženje; veze praćenja čuvaju se u oba smera (praćeni / pratioci) uz
  izlazni stepen, a blokade takođe u oba smera.
- **Zad 2 – PageRank:** iterativni PageRank (damping 0.85, epsilon 1e-6, obrada
  „dangling” čvorova); top korisnici preko heap-a; **warm start** pri ponovnom
  računanju nakon dodavanja novog korisnika ili nove veze.
- **Zad 3 – Pretraga:** pretraga po korisničkom imenu (tačno / prefiks /
  substring) i po rečima iz biografije preko **inverted index**-a; rezultati se
  rangiraju po relevantnosti, pa po PageRank vrednosti, uz heap. Tekst se
  normalizuje i tokenizuje; pretraga ne razlikuje velika i mala slova.
- **Zad 4 – Istorija:** hronološke liste koga je korisnik počeo da prati i ko
  je počeo da prati njega.
- **Zad 5 – Meni:** tekstualni meni koji povezuje sve funkcionalnosti i prikazuje ih korisniku.
- **Zad 6 – Trie + autocomplete:** prefiksno stablo korisničkih imena; dopune
  sortirane po PageRank vrednosti; ne razlikuje velika i mala slova.
- **Zad 7 – Hibridne preporuke:** `alpha * PPR + (1 - alpha) * sličnost`, gde je
  PPR **Personalized PageRank** iz perspektive korisnika, a sličnost se računa pomoću
  **Jaccard** ili **Cosine** nad biografijama; korisnik bira `alpha` i meru.
- **Zad 8 – BFS:** obilazak nivo po nivo do zadate dubine, svaki korisnik se
  obrađuje samo jednom.
- **Zad 9 – „Da li ste mislili”:** predlozi na osnovu Levenštajn rastojanja kada
  korisničko ime nije pronađeno.
- **Zad 10 – Blokiranja:** blokirani korisnici (u bilo kom smeru) se nikada ne
  preporučuju, a veza praćenja se odbija ako postoji blokiranje u bilo kom smeru.
- **Zad 11 – Kvalitet:** kod je podeljen u fokusirane module (jedan po
  funkcionalnosti), ovaj README i `PERFORMANCE.md`.
- **Zad 12 – Efikasnost:** sve strukture se grade jednom pri pokretanju i
  ponovo koriste; samo se PageRank ponovo računa nakon dodavanja korisnika ili
  veze (warm start). Vremena su u `PERFORMANCE.md`.

## Primeri (nad priloženim small skupom)

- **Pretraga po imenu:** `reece` (prefiks) ili `guimanja` (tačno).
- **Pretraga po biografiji:** `music love` ili `paramore`.
- **Autocomplete:** prefiks `ree` -> `reece99`.
- **BFS:** korisnik `1` (`guimanja`), maksimalni nivo `3`.
- **Preporuke:** korisnik `1`, `alpha = 0.6`, mera `jaccard`.
- **Najuticajniji:** opcija 3 izlistava korisnike sa najvećim PageRank-om.
- **Dodavanje korisnika:** opcija 4, npr. `id = 999999`, ime `novi_korisnik`,
  biografija `machine learning python developer`.

Primeri zavise od skupa podataka; uz medium/full izaberite bilo koji id ili ime
prikazano kroz pretragu i autocomplete.

## Organizacija projekta

```
projekat2_sv_54_2025/
├── data/{small,medium,full}/   # users.txt, connections.txt, blocked.txt
├── src/
│   ├── models.py           # User, SocialGraph                      (Zad 1)
│   ├── loader.py           # čitanje i parsiranje fajlova           (Zad 1, 12)
│   ├── pagerank.py         # iterativni PageRank + warm start       (Zad 2)
│   ├── ppr.py              # Personalized PageRank                  (Zad 7)
│   ├── text_processing.py  # normalizacija + tokenizacija           (Zad 3, 7)
│   ├── inverted_index.py   # inverted index nad biografijama        (Zad 3)
│   ├── search.py           # pretraga po imenu + bio, rangiranje    (Zad 3)
│   ├── trie.py             # trie + autocomplete                    (Zad 6)
│   ├── bfs.py              # BFS po nivoima                         (Zad 8)
│   ├── did_you_mean.py     # slična korisnička imena                (Zad 9)
│   ├── similarity.py       # Jaccard / Cosine                       (Zad 7)
│   ├── recommend.py        # hibridne preporuke + blokade           (Zad 7, 10)
│   ├── history.py          # istorija interakcija                   (Zad 4)
│   ├── app.py              # centralna klasa: gradi sve jednom      (Zad 12)
│   └── menu.py             # tekstualni meni                        (Zad 5)
├── main.py                 # ulazna tačka: bira skup, pokreće meni
├── README.md
└── PERFORMANCE.md          # merenja vremena za full skup           (Zad 12)
```
