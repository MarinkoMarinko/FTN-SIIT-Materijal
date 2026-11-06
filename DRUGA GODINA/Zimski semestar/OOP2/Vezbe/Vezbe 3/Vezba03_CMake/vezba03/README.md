# OOP2 - Vežba 3: Kalkulator

**Tekst zadatka:** [`vezba3.pdf`](vezba3.pdf) (originalni PDF iz materijala za vežbu, bez izmena).

U ovom paketu programi se prevode pomoću **CMake-a** (ili, opciono, GNU Make-a),
bez obaveze korišćenja Visual Studio IDE-a. U originalnom PDF-u piše da treba
koristiti Visual Studio za kontrolisano izvršavanje; za ovu verziju vežbe
može se koristiti **bilo koji debager** (GDB, LLDB ili debager u izabranom IDE-u).

## Preduslovi

- CMake 3.16 ili noviji;
- C++ kompajler sa podrškom za C++17 (GCC, Clang ili MSVC);
- instaliran odgovarajući alat za izgradnju projekta (npr. Make ili Ninja;
  na Windows-u može i MSVC generator).

Komande se izvršavaju **u korenskom direktorijumu `vezba03`**, u kojem se
nalazi `CMakeLists.txt` (ne u `SimpleCalculator` ili `AdvancedCalculator`).

## 1. Konfiguracija projekta (CMake)

Linux / macOS / Windows uz Make ili Ninja generator:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
```

Ovo se obično radi jednom na početku. Opcija `Debug` omogućava pogodniju
kompilaciju za debagovanje. Ako okruženje koristi višekonfiguracioni generator
(npr. Visual Studio), `Debug` se bira pri kompilaciji pomoću `--config Debug`.

## 2. Kompilacija

Svaki kalkulator je zaseban CMake target. Može se prevesti pojedinačno:

```bash
cmake --build build --target simple_calculator
cmake --build build --target advanced_calculator
```

Ili oba zajedno:

```bash
cmake --build build
```

Za višekonfiguracione generatore upotrebiti, na primer:

```bash
cmake --build build --config Debug --target simple_calculator
```

Nakon izmene C++ koda **nije potrebno ponovo pokretati konfiguraciju**;
dovoljno je ponoviti komandu za kompilaciju.

**VAŽNO:** Datoteke `calculator02buggy.cpp` i `calculator08buggy.cpp` sadrže
**namerno ostavljene greške**. Početna kompilacija zato *treba* da prijavi greške.
To je deo zadatka iz PDF-a, a ne problem sa CMake-om. Ispravljajte greške u
izvornom kodu, jednu po jednu, i ponovite kompilaciju.

## 3. Pokretanje programa (nakon uspešne kompilacije)

Na Linux-u i macOS-u, za standardni jednokonfiguracioni generator:

```bash
./build/simple_calculator
./build/advanced_calculator
```

Na Windows-u, u PowerShell-u, putanja zavisi od generatora:

```powershell
.\build\Debug\simple_calculator.exe  # npr. Visual Studio generator
.\build\simple_calculator.exe        # npr. Ninja generator
```

Isto važi za `advanced_calculator.exe`. Ako program nije uspešno preveden,
izvršna datoteka neće postojati.

## 4. Debagovanje

Koristite `Debug` konfiguraciju. Primeri nakon uspešne kompilacije:

```bash
gdb ./build/simple_calculator   # Linux / okruženje sa GDB-om
lldb ./build/simple_calculator  # macOS / okruženje sa LLDB-om
```

U GDB-u su korisne komande `break main`, `run`, `next`, `step` i `print`.
U LLDB-u: `breakpoint set --name main`, `run`, `next`, `step` i `frame variable`.
Moguće je koristiti i debager iz VS Code-a, CLion-a ili drugog editora.

## 5. Alternativa: GNU Make bez CMake-a

U istom direktorijumu dostupan je i jednostavan `Makefile`:

```bash
make simple      # osnovni kalkulator
make advanced    # napredni kalkulator
make             # oba
make clean       # briše build-make/
```

Nakon uspešne kompilacije izvršne datoteke su u `build-make/`:

```bash
./build-make/simple_calculator
./build-make/advanced_calculator
```

## Struktura projekta

```text
vezba03/
├── vezba3.pdf                        # originalni zadatak (neizmenjen)
├── README.md                         # ova uputstva
├── CMakeLists.txt                    # preporučeni način kompilacije
├── Makefile                          # alternativa bez CMake-a
├── SimpleCalculator/
│   ├── calculator02buggy.cpp         # zadatak: ispraviti greške
│   └── std_lib_facilities.h          # prateći C++17-kompatibilan header
└── AdvancedCalculator/
    ├── calculator08buggy.cpp         # zadatak: ispraviti greške
    └── std_lib_facilities.h          # prateći C++17-kompatibilan header
```

**Napomena:** Izvorne `.cpp` datoteke su iste kao u originalnom materijalu.
Prateći `std_lib_facilities.h` prilagođen je savremenim C++ kompajlerima;
ne sadrži rešenja zadataka.
