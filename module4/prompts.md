# Python Hash Functions & Password Security
*A Q&A study guide*

---

## Q1: Why does a simple hash function use `* 31`?

```python
hash_value = hash_value * 31 + ord(c)
```

The number **31** is a prime number, and that's the key reason it's chosen.

### Why primes reduce collisions
When you multiply by a prime, results spread more evenly across possible hash values. Non-prime multipliers tend to create patterns that cause different inputs to land on the same hash (a "collision"). Primes disrupt those patterns.

### Why 31 specifically is efficient
Compilers can optimize `x * 31` into a faster operation:
```
x * 31  ==  (x << 5) - x
```
That's a **bit-shift** (super fast) minus one subtraction — no actual multiplication needed.

### Why 31 is the right size
Too small (like 2 or 3) and similar strings cluster together. Too large and you overflow in unpredictable ways. 31 sits in a sweet spot.

### Example
```python
def simple_hash(s):
    hash_value = 0
    for c in s:
        hash_value = hash_value * 31 + ord(c)
    return hash_value

# "cat" vs "tac" — same letters, different order
print(simple_hash("cat"))   # 98262
print(simple_hash("tac"))   # 115836
```

> **Bottom line:** 31 is prime (reduces collisions), fast for hardware (bit-shift trick), and well-tested — Java's `String.hashCode()` uses the exact same multiplier.

---

## Q2: If a dictionary of usernames + hashed passwords was stolen, how crackable would it be?

**Very crackable.** Here's why:

### Problem 1 — No salt
Every user with the same password gets the **identical hash**. An attacker can immediately spot shared passwords:
```python
users = {
    "alice": 98262,
    "bob":   98262,   # attacker knows alice and bob share a password
}
```

### Problem 2 — It's too fast
Real password hashing (like bcrypt) is *intentionally slow* — hundreds of ms per attempt. A simple hash runs in **nanoseconds**, meaning an attacker can try billions of guesses per second.

### Problem 3 — No standard = no protection
Tools like **hashcat** and **John the Ripper** have built-in cracking support. A simple custom hash is actually *easier* to crack because it's simple math with no complexity.

### A Real Attack Scenario
```python
stolen_db = {"alice": 98262, "bob": 3198387}
common_passwords = ["password", "123456", "letmein", "cat", "qwerty"]

for username, stolen_hash in stolen_db.items():
    for guess in common_passwords:
        if simple_hash(guess) == stolen_hash:
            print(f"Cracked {username}: {guess}")

# Output: Cracked alice: cat
```

### What Should Be Used Instead

| Feature | Simple Hash | bcrypt |
|---|---|---|
| Salt | ❌ None | ✅ Unique per user |
| Speed | ❌ Nanoseconds | ✅ Intentionally slow (~300ms) |
| Collision resistance | ❌ Weak | ✅ Strong |
| Reversible patterns | ❌ Yes | ✅ No |

```python
import bcrypt

password = b"cat"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())  # unique salt baked in

# Verify later
bcrypt.checkpw(b"cat", hashed)  # True
```

---

## Q3: Does adding a simple salt make it harder to crack?

**Yes — meaningfully better, but not fully secure.**

### Implementation
```python
import random
import string

def generate_salt(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def simple_hash(s):
    hash_value = 0
    for c in s:
        hash_value = hash_value * 31 + ord(c)
    return hash_value

def register_salted_user(username: str, password: str) -> dict:
    salt = generate_salt(8)
    combined = password + salt
    hashed_password = simple_hash(combined)
    return {"username": username, "hashed_password": hashed_password, "salt": salt}

def login_salted_user(user_record: dict, attempted_password: str) -> bool:
    salt = user_record["salt"]
    combined = attempted_password + salt
    return simple_hash(combined) == user_record["hashed_password"]
```

### What the Salt Fixes ✅
- **No more identical hashes** — two users with `"cat"` now look completely different
- **Pre-built rainbow tables are useless** — attackers' lookup tables break because they'd need a separate table for every possible salt

### What's Still Weak ⚠️

**`random` is not cryptographically secure.** Python's `random` module is predictable. Use `secrets` instead:
```python
import secrets
secrets.choice(string.ascii_letters + string.digits)
```

**The hash is still fast.** A targeted brute-force attack on one user is still fast — the attacker just uses the known salt with millions of guesses.

**Length 8 is okay, but 16+ is better.** More salt characters = exponentially harder to brute force.

### Full Comparison

| Threat | No Salt | Salted Simple Hash | bcrypt |
|---|---|---|---|
| Rainbow tables | ❌ Cracked instantly | ✅ Defeated | ✅ Defeated |
| Two users same password | ❌ Obvious | ✅ Hidden | ✅ Hidden |
| Targeted brute force | ❌ Very fast | ⚠️ Still fast | ✅ Slow by design |
| Predictable salt generation | ❌ | ⚠️ Use `secrets` | ✅ Built in |

