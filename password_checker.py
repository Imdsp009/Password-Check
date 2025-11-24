def check_password(pw):
    if not any(char.isdigit() for char in pw):
        return "❌ Must contain a number"
    return "✔ Number OK"
