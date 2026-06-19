import secrets
import string


def ask_yes_no(prompt):
    return input(prompt).strip().lower() in ("y", "yes")


def generate_password(length, include_uppercase, include_digits, include_symbols):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()"

    # Step 3: Build pool starting with lowercase
    pool = lowercase
    required_chars = []

    if include_uppercase:
        pool += uppercase
        required_chars.append(secrets.choice(uppercase))

    if include_digits:
        pool += digits
        required_chars.append(secrets.choice(digits))

    if include_symbols:
        pool += symbols
        required_chars.append(secrets.choice(symbols))

    # Always ensure at least one lowercase (since lowercase is always included)
    required_chars.append(secrets.choice(lowercase))

    # Minimum length check for guarantee logic
    if length < len(required_chars):
        raise ValueError(
            f"Length must be at least {len(required_chars)} for selected options."
        )

    # Step 4: Fill remaining length with random chars from pool
    remaining = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(pool) for _ in range(remaining)]

    # Shuffle securely (Fisher-Yates using secrets.randbelow)
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: ").strip())
        if length <= 0:
            print("Please enter a positive number.")
            return

        include_uppercase = ask_yes_no("Include uppercase? (Y/N): ")
        include_digits = ask_yes_no("Include digits? (Y/N): ")
        include_symbols = ask_yes_no("Include symbols? (Y/N): ")

        password = generate_password(
            length, include_uppercase, include_digits, include_symbols
        )

        # Step 5: Display result
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()