def escape_html(message: str): # From Lecture Example HTML Injection Attacks
    return message.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def replace_spaces(message: str): # Replaces the '+' with actual spaces
    return message.replace('+', ' ')

def replace_encoded(message: str): # Replaces special encoded characters to their actual characters
    return message.replace('%27', "'").replace('%21', '!').replace('%40', '@').replace('%23', '#').replace('%24', '$').replace('%5E', '^').replace('%26', '&').replace('%28', '(').replace('%29', ')').replace('%2D', '-').replace('%5F', '_').replace('%3D', '=').replace('%3F', '?').replace('%2B', '+').replace('+', ' ').replace('%25', '%')

# Not used yet
def file_size(path: str): # For Content Length
    with open(path, 'rb') as file:
        length = len(file.read())
        file.close()
        return length
    
def file_string(path: str): # For Response Body
    with open(path, 'rb') as file:
        string = file.read()
        file.close()
        return string
    
