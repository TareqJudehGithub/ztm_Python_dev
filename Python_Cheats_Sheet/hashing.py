"""
Hashing 101

- Hashing is decrpting simple strings.
- Idempotent is converting hashed chars into simple strings.
- SHA-1 is a popular example of hashing.
- IN python, we use hashlib built-in libray
 import hashlib
 sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

"""

