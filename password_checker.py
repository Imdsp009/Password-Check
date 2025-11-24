def check_password(password):
    if len(password) < 8:
        return "❌ Too short"
    if not any(c.isdigit() for c in password):
        return "❌ Must contain a number"
    return "🟡 Medium strength"
