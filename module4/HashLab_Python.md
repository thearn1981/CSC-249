# CSC 249 - Hash Tables Lab: Password Hashing & Salting (Python Edition)
**Module: Hash Tables — From Convention Lines to Cryptography**

---

## 📋 SUBMISSION REQUIREMENTS
- **File Name**: `hash_lab_yourname.py`
- **Submit**: GitHub pull request
- **Points**: 100 total (25 + 35 + 40)
- **AI Use**: MANDATORY — Save your prompts in `prompts.txt`

---

## 🎯 WHAT YOU'RE BUILDING

A working password registration and login system that demonstrates three real-world applications of hashing:

1. **A Simple Hash Function** — Turn a string into a number (the same concept that assigns convention attendees to check-in lines)
2. **Password Storage** — Store hashed passwords instead of plaintext (why the Ashley Madison breach could have been less catastrophic)
3. **Salted Password Storage** — Add randomness so identical passwords don't produce identical hashes (why rainbow tables fail)

By the end of this lab you will have built something that every production authentication system on earth uses some version of. This is not academic — this is Tuesday at work.

---

## 🧠 THE CONCEPT IN 60 SECONDS

Remember the convention check-in analogy: a single line is slow, so you split attendees into bins by last name (A–J, K–Z). The function that decides which bin you go to — that's a hash function. The bins themselves — that's a hash table.

Now apply the same idea to passwords:

- A hash function takes a password string and produces a fixed output (a hash).
- The same input always produces the same output.
- But you **cannot reverse** the output back to the input. It's one-way.
- This means you can check "did they type the right password?" without ever storing the password itself.

The problem: if two users both pick "123456" as their password, they get the same hash. An attacker with a list of common password hashes (a rainbow table) can match them instantly. The fix: add a random **salt** to each password before hashing, so "123456" hashes differently for every user.

---

## 🔧 WHAT YOU NEED

Standard library only. No `pip install` required.

```python
import random
import string
import time
```

**Note on Python's built-in `hash()`**: Python has a built-in `hash()` function, but it's randomized per session by default (for security reasons). We're writing our own so you understand what's happening inside. Do not use the built-in `hash()` for this lab.

---

## 📝 THE EXERCISES

### Exercise 1: Build a Simple Hash Function (25 points)
**The Pattern**: Turn a string into a number, deterministically.

Write a function `hash_password(password: str) -> int` that:

- Iterates through each character of the password
- Uses each character's ASCII value (via `ord()`) to build up a hash
- Returns a numeric hash value

**A working approach** (you can use this or design your own):
```
hash_value = 0
for each character c in password:
    hash_value = hash_value * 31 + ord(c)
return hash_value
```

**What to demonstrate**:
- Hash "password" and print the result
- Hash "password" again — it must produce the **same** result
- Hash "Password" (capital P) — it must produce a **different** result
- Hash "123456" and print the result

**Why 31?** It's a prime number. Primes distribute values more evenly across bins — fewer collisions. This is the same tradeoff from the convention check-in slides: you want your hash function to spread people (or passwords) evenly, not pile them all into one line.

**Test your function before moving on.**

---

### Exercise 2: Password Registration and Login (35 points)
**The Pattern**: Store the hash, never the password.

Use a dictionary to represent a user record:

```python
# A user record looks like this:
# {"username": "alice", "hashed_password": 283746591}
```

**Function 1: `register_user(username: str, password: str) -> dict`**
- Hash the password using your function from Exercise 1
- Return a dictionary with `"username"` and `"hashed_password"` keys
- Print a confirmation: `"User [username] registered. Stored hash: [hash]"`

**Function 2: `login_user(user_record: dict, attempted_password: str) -> bool`**
- Hash the attempted password
- Compare it to the stored hash
- Return True if they match, False otherwise
- Print the result: `"Login successful"` or `"Login failed"`

**What to demonstrate**:
- Register a user with username "alice" and password "securePass99"
- Attempt login with the correct password → should succeed
- Attempt login with "securepass99" (wrong case) → should fail
- Attempt login with "wrongpassword" → should fail
- Print what's actually stored in the user record (username + hash, **not** the original password)

**The takeaway**: At no point does your program store "securePass99" in the dictionary. If someone stole your user record, they'd have a hash — not a password.

**Python bonus insight**: Notice that your user record is itself a dictionary — Python's built-in hash table. You're using a hash table to store hashed passwords. Hashing all the way down.

---

### Exercise 3: Add Salting (40 points)
**The Pattern**: Same password + different salt = different hash.

Upgrade your user record:

```python
# A salted user record looks like this:
# {"username": "bob", "hashed_password": 9182736, "salt": "xK4mQ9pL"}
```

**Function: `generate_salt(length: int) -> str`**
- Generate a random string of the given length
- Use characters from: `string.ascii_letters + string.digits`
- Use `random.choice()` to pick each character

**Function: `register_salted_user(username: str, password: str) -> dict`**
- Generate a salt (length 8)
- Concatenate: `password + salt`
- Hash the combined string
- Return a dictionary with `"username"`, `"hashed_password"`, and `"salt"` keys

**Function: `login_salted_user(user_record: dict, attempted_password: str) -> bool`**
- Load the salt from the user record
- Concatenate: `attempted_password + user_record["salt"]`
- Hash the combined string
- Compare to stored hash

**What to demonstrate**:
- Register two different users ("bob" and "carol") who **both** use the password "123456"
- Print both user records — show that the salts are different and the hashes are different, even though the passwords are identical
- Log in as bob with "123456" → should succeed
- Log in as bob with "654321" → should fail
- Log in as carol with "123456" → should succeed

**The takeaway**: Without salting, an attacker who cracks one "123456" hash has cracked every account using that password. With salting, each account is a separate problem. This is why the rainbow table on slide 20 of the lecture becomes useless — those precomputed hashes don't account for per-user salts.

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Storing the password**: Your user record dictionary should never contain a `"password"` key. The whole point is that you don't keep it.

2. **Using Python's built-in `hash()`**: It's randomized per session. Your hash function must be deterministic — same input, same output, every time, every run.

3. **Comparing strings instead of hashes**: In your login function, hash the attempt first, then compare hashes. Don't compare the raw password to anything stored.

4. **Concatenation order**: Be consistent. If you register with `password + salt`, you must log in with `password + salt` — not `salt + password`.

---

## ✅ TESTING YOUR CODE

### Exercise 1 Checklist:
- [ ] Same input always produces same hash
- [ ] Different inputs produce different hashes
- [ ] Small changes (capitalization) produce different hashes
- [ ] Running the script twice gives the same hashes (deterministic)

### Exercise 2 Checklist:
- [ ] Correct password logs in successfully
- [ ] Wrong password is rejected
- [ ] User record contains hash, not plaintext password
- [ ] Program never prints the original password from storage

### Exercise 3 Checklist:
- [ ] Two users with same password get different hashes
- [ ] Two users with same password get different salts
- [ ] Login still works correctly with salting
- [ ] Salt is stored alongside the hash (it's not secret — it just needs to be unique)

---

## 🔗 CONNECTION TO HASH TABLES

You just built the **cryptographic application** of hashing. Here's how it connects to the **data structure**:

| Concept | Hash Table (Data Structure) | Password Hashing (Cryptography) |
|---|---|---|
| Hash function | Maps key → array index (bin) | Maps password → fixed numeric output |
| Collision | Two keys land in same bin | Two passwords produce same hash (rare but possible) |
| One-way? | No — you can retrieve values | Yes — you cannot recover the password from the hash |
| Salt equivalent | Load factor / resize strategy | Random per-user string to prevent rainbow attacks |

The hash function you wrote in Exercise 1 is conceptually the same function that decides which "convention check-in line" a name goes to. In a hash table, it maps keys to bucket indices. In password security, it maps passwords to stored verification values. Same math, different applications.

**Python-specific connection**: Every time you use a `dict`, Python is calling a hash function on your key to decide which internal bucket to store the value in. The `dict` you used to store your user records is itself a hash table. When you wrote `user_record["username"]`, Python hashed the string `"username"` to find the right bucket. Your Exercise 1 hash function does the same thing Python's internals do.

---

## 🚀 BONUS CHALLENGES (+10 points max)

- **+3**: Store multiple users in a list of dictionaries and implement a `find_user(username)` lookup function (now you're building a hash table's interface — or just use a dict of dicts keyed by username, and explain why that's already a hash table)
- **+3**: Add a "change password" feature that generates a new salt
- **+4**: Implement a brute-force cracker that tries every 4-character lowercase password against an unsalted hash — then show how much longer it takes against a salted hash (time it with `time.time()`)

---

## 💡 WORKING WITH AI

You are required to use AI tools for this lab. Good uses:

- "Explain why multiplying by a prime number helps distribute hash values"
- "What happens if my salt is too short?"
- "Why does Python randomize its built-in hash() function?"
- "Show me how the login verification flow works step by step"
- "What's the difference between my teaching hash function and what bcrypt does?"

Document your AI conversations in `prompts.txt`. This is part of your grade — it shows your learning process.

---

## 📚 CONTEXT: WHY THIS MATTERS AT WORK

Every web application, mobile app, and API you will ever work on handles authentication. The pattern you just built — hash the password, store the hash, verify by re-hashing — is not a textbook exercise. It's the actual architecture. Production systems use stronger hash functions (bcrypt, scrypt, Argon2) and longer salts, but the logic is identical to what you wrote today.

When a company gets breached and the headline says "passwords were stored in plaintext" — that means they skipped what you just built. When the headline says "passwords were hashed and salted" — that means they did exactly this.

You now understand both sides of that headline.
