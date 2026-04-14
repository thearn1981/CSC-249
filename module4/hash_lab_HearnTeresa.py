import random
import string
import time

def find_user(users, username):
    """
    Finds and returns a user record by username.
    Returns None if not found.
    """
    for user in users:
        if user["username"] == username:
            return user
    return None

def change_salted_password(user_record: dict, new_password: str) -> None:
    """
    Changes a salted user's password by generating a new salt
    and storing a new salted hash.
    """
    new_salt = generate_salt(8)
    new_hash = hash_password(new_password + new_salt)

    user_record["salt"] = new_salt
    user_record["hashed_password"] = new_hash

    print(f"Password changed for {user_record['username']}.")
def brute_force_unsalted_hash(target_hash: int, max_length: int = 4):
    """
    Attempts to crack an unsalted hash using lowercase passwords
    up to max_length characters.
    """
    chars = string.ascii_lowercase

    for a in chars:
        if hash_password(a) == target_hash:
            return a

        for b in chars:
            attempt = a + b
            if hash_password(attempt) == target_hash:
                return attempt

            for c in chars:
                attempt = a + b + c
                if hash_password(attempt) == target_hash:
                    return attempt

                for d in chars:
                    attempt = a + b + c + d
                    if hash_password(attempt) == target_hash:
                        return attempt

    return None

def brute_force_salted_hash(target_hash: int, salt: str, max_length: int = 4):
    """
    Attempts to crack a salted hash using lowercase passwords
    up to max_length characters.
    """
    chars = string.ascii_lowercase

    for a in chars:
        if hash_password(a + salt) == target_hash:
            return a

        for b in chars:
            attempt = a + b
            if hash_password(attempt + salt) == target_hash:
                return attempt

            for c in chars:
                attempt = a + b + c
                if hash_password(attempt + salt) == target_hash:
                    return attempt

                for d in chars:
                    attempt = a + b + c + d
                    if hash_password(attempt + salt) == target_hash:
                        return attempt

    return None



def hash_password(password):
    ''' 
     Generates a deterministic numeric hash from a password string
    by iterating through each character and combining ASCII values.
    '''
    hash_value = 0
    for c in password:
        hash_value = hash_value * 31 + ord(c)
    return hash_value


def register_user(username: str, password: str) -> dict:
    """
    Registers a user by storing username and hashed password.
    """
    hashed = hash_password(password)
    user_record = {
        "username": username,
        "hashed_password": hashed
    }
    print(f"User {username} registered. Stored hash: {hashed}")
    return user_record


def login_user(user_record: dict, attempted_password: str) -> bool:
    """
    Attempts login by comparing hashed passwords.
    """
    attempted_hash = hash_password(attempted_password)

    if attempted_hash == user_record["hashed_password"]:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False
    
def generate_salt(length: int) -> str:
    """
    Generates a random salt string using letters and digits.
    """
    characters = string.ascii_letters + string.digits
    salt = ""
    for _ in range(length):
        salt += random.choice(characters)
    return salt


def register_salted_user(username: str, password: str) -> dict:
    """
    Registers a user by generating a salt and storing the salted hash.
    """
    salt = generate_salt(8)
    hashed = hash_password(password + salt)

    user_record = {
        "username": username,
        "hashed_password": hashed,
        "salt": salt
    }

    print(f"User {username} registered.")
    return user_record


def login_salted_user(user_record: dict, attempted_password: str) -> bool:
    """
    Attempts login by hashing the attempted password with the stored salt.
    """
    salt = user_record["salt"]
    attempted_hash = hash_password(attempted_password + salt)

    if attempted_hash == user_record["hashed_password"]:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False    
    
def main():
        

        # -----------------------------
        # 🔍 PART 1: Hash Function Demo
        # -----------------------------
        print("=" * 40  + " PART 1: Hash Function Demo " + "=" * 40)
        print()
        print("Hash of 'password':", hash_password("password"))

        # Same input → same hash
        print("Hash of 'password' again:", hash_password("password"))

        # Different case → different hash
        print("Hash of 'Password':", hash_password("Password"))

        # Numbers
        print("Hash of '123456':", hash_password("123456"))


        # -----------------------------
        # 🔐 PART 2: User System Demo
        # -----------------------------
        print("=" * 40  + " PART 2: User System Demo " + "=" * 40)

        # Register user
        user = register_user("alice", "securePass99")

        # Show stored data (NO plain password)
        print("Stored user record:", user)

        # Correct login
        print("Attempting correct login:")
        login_user(user, "securePass99")

        # Wrong case
        print("Attempting login with wrong case:")
        login_user(user, "securepass99")

        # Completely wrong password
        print("Attempting login with wrong password:")
        login_user(user, "wrongpassword")
    
        # -----------------------------
        # 🔍 Demonstration
        # -----------------------------
        print("=" * 40  + " PART 3: Salting Demo " + "=" * 40)
        # Register two users with the SAME password
        bob = register_salted_user("bob", "123456")
        carol = register_salted_user("carol", "123456")

        # Print both records
        print("Bob's record:", bob)
        print("Carol's record:", carol)

        # Bob correct password
        print("Bob attempts login with '123456':")
        login_salted_user(bob, "123456")

        # Bob wrong password
        print("Bob attempts login with '654321':")
        login_salted_user(bob, "654321")

        # Carol correct password
        print("Carol attempts login with '123456':")
        login_salted_user(carol, "123456")                

        # -----------------------------
        # EXTRA: Multiple Users Demo
        # -----------------------------
        print( "=" * 40 + " EXTRA: Multiple Users " + "=" * 40)

        users = []
        users.append(register_user("alice", "securePass99"))
        users.append(register_salted_user("bob", "123456"))
        users.append(register_salted_user("carol", "123456"))

        print("Finding bob:")
        print(find_user(users, "bob"))

        print("Finding dave:")
        print(find_user(users, "dave"))


        # -----------------------------
        # EXTRA: Change Password Demo
        # -----------------------------
        print("" + "=" * 40 + " EXTRA: Change Password " + "=" * 40)

        print("Bob before password change:", bob)
        change_salted_password(bob, "newpass123")
        print("Bob after password change:", bob)

        print("Trying bob's old password:")
        login_salted_user(bob, "123456")

        print("Trying bob's new password:")
        login_salted_user(bob, "newpass123")


        # -----------------------------
        # EXTRA: Brute Force Demo
        # -----------------------------
        print( "=" * 40 + " EXTRA: Brute Force Demo " + "=" * 40)

        demo_password = "able"

        # Unsalted
        unsalted_hash = hash_password(demo_password)
        start = time.time()
        cracked = brute_force_unsalted_hash(unsalted_hash, 4)
        end = time.time()

        print("Unsalted target hash:", unsalted_hash)
        print("Recovered password:", cracked)
        print("Time:", round(end - start, 4), "seconds")

        # Salted
        demo_salt = generate_salt(8)
        salted_hash = hash_password(demo_password + demo_salt)
        start = time.time()
        cracked = brute_force_salted_hash(salted_hash, demo_salt, 4)
        end = time.time()

        print("Salted target hash:", salted_hash)
        print("Salt:", demo_salt)
        print("Recovered password:", cracked)
        print("Time:", round(end - start, 4), "seconds")


    

if __name__ == "__main__":
    main()
