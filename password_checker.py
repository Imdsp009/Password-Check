def check_password(password):
    if len(password) < 8:
        return "❌ Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "❌ Weak: Password must contain at least one number."
    return "🟡 Medium Strength"
