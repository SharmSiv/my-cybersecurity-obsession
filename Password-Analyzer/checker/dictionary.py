from pathlib import Path
import re

class DictionaryCheck:
    LEET_MAP = {
        "0": "o",
        "1": "i",
        "3": "e",
        "4": "a",
        "@": "a",
        "$": "s",
        "5": "s",
        "7": "t",
        "8": "b"
    }

    def __init__(self):
        self.words = set()
        path = Path("dictionary/english_words.txt")
        if not path.exists():
            raise FileNotFoundError(f"Missing dictionary file: {path}")
        with path.open(encoding="utf-8", errors="ignore") as file:
            self.words = {
                line.strip().lower()
                for line in file
                if line.strip()
            }

        print(f"Loaded {len(self.words):,} dictionary words.")

    def normalize_leetspeak(self, text):
        return "".join(
            self.LEET_MAP.get(char.lower(), char.lower())
            for char in text
        )

    def contains_dictionary_word(self, password):
        # First check the original password
        if self._check(password.lower()):
            return True

        # Then check a normalized version
        normalized = self.normalize_leetspeak(password)

        if self._check(normalized):
            return True

        return False

    def _check(self, text):
        # Extract alphabetic words only
        tokens = re.findall(r"[a-z]{4,}", text)
        for token in tokens:
            if token in self.words:
                return True

        return False