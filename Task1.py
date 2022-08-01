"""
There is string s = "Python Bootcamp". Write the code that hashes string.
"""
import hashlib

s = 'Python Bootcamp'
hashed_string = hashlib.sha256(s.encode())

print(hashed_string.hexdigest())
