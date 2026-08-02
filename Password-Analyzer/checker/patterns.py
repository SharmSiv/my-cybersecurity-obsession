import re


class PatternCheck:
    KEYBOARD = [
        "qwerty",
        "asdfgh",
        "zxcvbn",
        "12345",
        "23456",
        "34567",
        "45678",
        "56789",
        "abcdef",
        "bcdefg",
        "cdefgh"
    ]

    
    def repeated(self, password):
        return bool(re.search(r"(.)\1{2,}", password))


    def sequential(self, password):
        password = password.lower()
        return any(pattern in password for pattern in self.KEYBOARD)