def check_password(pw):
    if len(pw) < 8:
        return "❌ Too short"
    return "✔ Length OK"
