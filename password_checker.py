def check_password(password):
    special = "!@#$%^&*?"

    if len(password) < 8:
        return "❌ Too short"

    if not any(c.isdigit() for c in password):
        return "❌ Must contain a number"

    if not any(c.isupper() for c in password):
        return "❌ Must contain a capital letter"

    if not any(c in special for c in password):
        return "❌ Must contain a special character"

    return "🟢 Strong Password"
