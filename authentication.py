#helper functions for loggining in

def validate_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return False

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if password contains at least one special character
    special_chars = set('!@#$%^&*()_-+=[]{}|\\:;\'\"<>,.?/~')
    if not any(char in special_chars for char in password):
        return False

    return True


def extract_credentials(request):
    # Parse the request body to extract form data
    body = request.get_data(as_text=True)
    parts = body.split("&")
    username = parts[0].split("=")[1]
    password1 = parts[1].split("=")[1]
    password2 = parts[2].split("=")[1]

    return username, password1, password2
