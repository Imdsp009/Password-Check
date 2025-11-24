def check_password(password):
    special = "!@#$%^&*()?"
    
    if not any(char.isupper() for char in password):
        return "❌ Weak: Must contain one uppercase letter."
    if not any(char in special for char in password):
        return "❌ Weak: Must contain one special character."
    return "🟢 Strong password"
