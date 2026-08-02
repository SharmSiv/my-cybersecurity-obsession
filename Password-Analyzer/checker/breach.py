import hashlib
import requests


class HaveIBeenPwned:
    API_URL = "https://api.pwnedpasswords.com/range/"

    def pwned_check(self, password):
        #Return whether the password was found in a known data breach

        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        try:
            response = requests.get(
                self.API_URL + prefix,
                headers={"User-Agent": "PasswordAnalyzer"},
                timeout=5,
            )
            response.raise_for_status()

        except requests.RequestException:
            # Continue gracefully if the API cannot be reached.
            return False, None

        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")

            if hash_suffix == suffix:
                return True, int(count)

        return False, 0