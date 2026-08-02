from pathlib import Path


class CommonPasswords:
    def __init__(self):
        self.passwords = set()

        path = Path("passwords/common_passwords.txt")

        if not path.exists():
            raise FileNotFoundError(f"Missing password list: {path}")
            
        with path.open(encoding="utf-8", errors="ignore") as file:
            self.passwords = {
                line.strip().lower()
                for line in file
                if line.strip()
            }

        print(f"Loaded {len(self.passwords):,} common passwords.")

    def is_common(self, password):
        return password.lower() in self.passwords