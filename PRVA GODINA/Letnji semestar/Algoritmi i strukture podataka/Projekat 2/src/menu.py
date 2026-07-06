MENU = """
==================== Društvena mreza ====================
 1) Pretraga po korisničkom imenu
 2) Pretraga po biografiji
 3) Najuticajniji korisnici
 4) Dodaj novog korisnika
 5) Dodaj vezu praćenja
 6) Istorija interakcija korisnika
 7) Autocomplete korisničkog imena
 8) Obilazak mreže (BFS)
 9) Preporuka korisnika
 0) Izlaz
========================================================="""


class Menu:
    def __init__(self, app):
        self.app = app

    def _ask(self, prompt):
        return input(prompt).strip()

    def _ask_int(self, prompt, default = None):
        raw = self._ask(prompt)
        if raw == "" and default is not None:
            return default
        try:
            return int(raw)
        except ValueError:
            print("  Unesite ceo broj.")
            return None

    def _short_bio(self, bio, width = 60):
        bio = bio.strip()
        return bio if len(bio) <= width else bio[:width] + "..."

    def _show_user(self, user, suffix = ""):
        if user is None:
            return
        line = f"  {user.username} (id={user.id})"
        if suffix:
            line += f"  {suffix}"
        print(line)
        print(f"      biografija: {self._short_bio(user.bio)}")

    def _resolve_user(self, label = "korisnika"):
        raw = self._ask(f"Unesite {label} (id ili korisnicko ime): ")
        if raw == "":
            return None
        if raw.isdigit():
            user = self.app.get_user_by_id(int(raw))
            if user is None:
                print(f"  Ne postoji korisnik sa id {raw}.")
            return user
        user = self.app.get_user_by_username(raw)
        if user is None:
            print(f"  Ne postoji korisnik sa imenom '{raw}'.")
            suggestions = self.app.did_you_mean(raw)
            if suggestions:
                print("  Da li ste mislili: " + ", ".join(suggestions) + "?")
        return user
    
    def search_username(self):
        query = self._ask("Potražite korisnika (unesite korisnicko ime): ")
        results = self.app.search_username(query, k = 10)
        if not results:
            print("  Nema rezultata.")
            suggestions = self.app.did_you_mean(query)
            if suggestions:
                print("  Da li ste mislili: " + ", ".join(suggestions) + "?")
            return
        print(f"  Pronadjeno rezultata: {len(results)}")
        for user, _rel in results:
            self._show_user(user)

    def search_bio(self):
        query = self._ask("Potražite korisnika (unesite reči iz biografije): ")
        results = self.app.search_bio(query, k = 10)
        if not results:
            print("  Nema rezultata.")
            return
        print(f"  Top {len(results)} po relevantnosti i PageRank vrednosti:")
        for user, matches in results:
            self._show_user(user, suffix=f"[poklapanja reči: {matches}]")

    def top_influencers(self):
        k = self._ask_int("Koliko najuticajnijih želite? [10]: ", default = 10)
        if k is None or k <= 0:
            return
        print(f"  Top {k} po PageRank vrednosti:")
        for rank, (user, score) in enumerate(self.app.top_influencers(k), 1):
            self._show_user(user, suffix = f"[#{rank}, PR = {score:.6f}]")

    def add_user(self):
        print("Dodavanje novog korisnika (id se dodeljuje automatski).")
        username = self._ask("Unesite korisničko ime: ")
        bio = self._ask("Unesite biografiju: ")
        ok, message = self.app.add_user(username, bio)
        print(("  " + message) if ok else ("  Odbijeno: " + message))

    def add_follow(self):
        print("Dodavanje veze praćenja (A počinje da prati B).")
        a = self._resolve_user("korisnika A (pratilac)")
        if a is None:
            return
        
        b = self._resolve_user("korisnika B (praćen)")
        if b is None:
            return
        
        ok, message = self.app.add_follow(a.id, b.id)
        print(("  " + message) if ok else ("  Odbijeno: " + message))

    def interaction_history(self):
        user = self._resolve_user()
        if user is None:
            return
        
        following, followers = self.app.interaction_history(user.id)
        print(f"  Istorija za {user.username} (id={user.id}):")

        print(f"  -- Započeo da prati ({len(following)}), od najstarijeg:")
        if not following:
            print("      (nema)")
        for u in following:
            print(f"      -> {u.username} (id={u.id})")

        print(f"  -- Zapraćen(a) od strane ({len(followers)}), od najstarijeg:")
        if not followers:
            print("      (nema)")
        for u in followers:
            print(f"      <- {u.username} (id={u.id})")

    def autocomplete(self):
        prefix = self._ask("Prefiks korisničkog imena: ")
        if prefix == "":
            return
        
        results = self.app.autocomplete(prefix, k = 10)
        if not results:
            print("  Nema korisničkih imena sa tim prefiksom.")
            return
        
        print(f"  Dopune za '{prefix}' (po PageRank vrednosti):")
        for user, score in results:
            print(f"      {user.username} (id = {user.id}, PR = {score:.6f})")

    def explore_bfs(self):
        user = self._resolve_user()
        if user is None:
            return
        
        max_level = self._ask_int("Do kog nivoa želite pretragu? [3]: ", default = 3)
        if max_level is None or max_level < 1:
            return
        
        levels = self.app.bfs(user.id, max_level)
        if not levels:
            print("  Ovaj korisnik ne prati nikoga u zadatom opsegu.")
            return
        
        for level in sorted(levels):
            users = levels[level]
            print(f"  Nivo {level} ({len(users)} korisnika):")
            for u in users[:20]:
                print(f"      {u.username} (id = {u.id})")
            if len(users) > 20:
                print(f"      ... i još {len(users) - 20}")

    def recommend(self):
        user = self._resolve_user()
        if user is None:
            return
        
        alpha = self._ask("Unesite alpha od 0 do 1 (težina PageRank vs biografija) [0.5]: ")
        try:
            alpha = float(alpha) if alpha else 0.5
        except ValueError:
            alpha = 0.5
        alpha = min(1.0, max(0.0, alpha))

        measure = self._ask("Unesite sličnost 'jaccard' ili 'cosine' [jaccard]: ").lower()
        if measure not in ("jaccard", "cosine"):
            measure = "jaccard"

        print(f"  Preporuke za {user.username} "
              f"(alpha = {alpha}, {measure}):")
        
        results = self.app.recommend(user.id, alpha = alpha, k = 10, measure = measure)
        if not results:
            print("      (nema kandidata)")
            return
        
        for user_rec, score in results:
            self._show_user(user_rec, suffix=f"[skor={score:.4f}]")

    def run(self):
        actions = {
            "1": self.search_username,
            "2": self.search_bio,
            "3": self.top_influencers,
            "4": self.add_user,
            "5": self.add_follow,
            "6": self.interaction_history,
            "7": self.autocomplete,
            "8": self.explore_bfs,
            "9": self.recommend,
        }
        while True:
            print(MENU)
            choice = self._ask("Izaberite opciju: ")
            if choice == "0":
                print("Izlazak iz aplikacije...")
                return
            action = actions.get(choice)
            if action is None:
                print("Nepoznata opcija. Pokušajte ponovo.")
                continue
            try:
                action()
            except (EOFError, KeyboardInterrupt):
                print("\nIzlazak iz aplikacije...")
                return
            except Exception as exc:  # keep the menu alive on bad input
                print(f"Greška: {exc}")
