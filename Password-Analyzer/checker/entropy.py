import math
import re

def calc_entropy(password):
#Estimate entropy of password in bits
    if not password:
        return 0
    char_pool = 0

    #Determine size of the character pool
    if re.search(r"[a-z]", password):
        char_pool += 26

    if re.search(r"[A-Z]", password):
        char_pool += 26

    if re.search(r"\d", password):
        char_pool += 10

    if re.search(r"[^A-Za-z0-9]", password):
        char_pool += 32
        
    entropy_bits = len(password) * math.log2(char_pool)
    return round(entropy_bits, 2)