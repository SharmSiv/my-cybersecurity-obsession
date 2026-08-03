Password Analyzer is a tool I created for the purpose of checking the security of a password by using 
the following features:
- Entropy score (scores the randomness of the password).
- Detects dictionary words.
- Detects if the password is common.
- Have I Been Pwned (HIBP) breach detection (how many times the password was found in known breaches).
- Recommendations (Feedback on how to make password more secure).

Made with:
- Python, HTML5, CSS3, JavaScript.
- Flask
- HIBP API

This app does not store, log, or save passwords in any way. It uses SHA-1 cryptographic hashing with the HIPB k-anonymity model,
so the user's plain-text password is never transmitted through the internet, neither is the complete SHA-1 hash. Passwords are
analyzed in real-time in memory, and is immediately discarded after processing.

Give it a try here! [Password Analyzer](https://password-analyzer-0sbk.onrender.com/)
