import re

from checker.entropy import calc_entropy
from checker.dictionary import DictionaryCheck
from checker.patterns import PatternCheck
from checker.common import CommonPasswords
from checker.breach import HaveIBeenPwned


class PasswordAnalyzer:
    MAX_SCORE = 20

    def __init__(self):
        self.dictionary = DictionaryCheck()
        self.patterns = PatternCheck()
        self.common = CommonPasswords()
        self.breach = HaveIBeenPwned()

    def check(self, password):
        score = 0
        feedback = []

        #Score based on length
        if len(password) >= 16:
            score += 4
        elif len(password) >= 12:
            score += 3
        elif len(password) >= 8:
            score += 2
        else:
            feedback.append("Password must be at least 8 characters.")


        #Reward the use of diverse characters
        if re.search(r"[A-Z]", password):
            score += 2
        else:
            feedback.append("Add uppercase letters.")


        if re.search(r"[a-z]", password):
            score += 2
        else:
            feedback.append("Add lowercase letters.")


        if re.search(r"\d", password):
            score += 2
        else:
            feedback.append("Add numbers.")


        if re.search(r"[^A-Za-z0-9]", password):
            score += 2
        else:
            feedback.append("Add special characters.")


        #Penalize repeated characters
        if self.patterns.repeated(password):
            score -= 2
            feedback.append("Try to avoid repeated characters.")
        else:
            score += 1
            
        entropy = calc_entropy(password)
            
        if entropy >= 80:
            score += 2            
        elif entropy >= 60:
            score +=1
        else:
            feedback.append("Password could be more random")
            

        #Penalise predictable patterns
        if self.patterns.sequential(password):
            score -= 3
            feedback.append("Avoid keyboard or sequential patterns.")
        else:
            score += 2

        if self.dictionary.contains_dictionary_word(password):
            score -= 3
            feedback.append("Avoid dictionary words.")
        else:
            score += 2

        
        if self.common.is_common(password):
            score -= 8
            feedback.append("This is a very common password.")
        else:
            score += 1
            
            
        breached, breach_count = self.breach.pwned_check(password)
        if breached:
            score -= 4
            feedback.append(
                f"This password has appeared in {breach_count:,} known data breaches."
            )
        else:
            score += 1
            
        score = max(0, min(score, self.MAX_SCORE))
        if score <= 8:
            strength = "Too weak"
            color = "red"
        elif score <= 12:
            strength = "Still a bit weak"
            color = "orange"
        elif score <= 16:
            strength = "Okay, but could be stronger"
            color = "gold"
        elif score <= 18:
            strength = "Quite strong"
            color = "limegreen"
        else:
            strength = "Very strong. Perfect!"
            color = "green"
    
        return {
            "score": score,
            "max_score": self.MAX_SCORE,
            "strength": strength,
            "feedback": feedback,
            "color": color,
            "entropy": entropy,
            "breached": breached,
            "breach_count": breach_count
        }