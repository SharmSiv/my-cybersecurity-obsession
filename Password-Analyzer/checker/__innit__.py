def __init__(self):
    self.dictionary = DictionaryCheck()
    self.patterns = PatternCheck()
    self.common = CommonPasswords()
    self.breach = HaveIBeenPwned()