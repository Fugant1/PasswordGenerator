import random
import string

def create_password(length, uppercase, lowercase, numbers, symbols):
    elements = ''
    if uppercase:
        elements += string.ascii_uppercase
    if lowercase:
        elements += string.ascii_lowercase
    if numbers:
        elements += string.digits
    if symbols:
        elements += string.punctuation
    password = ''.join(random.choice(elements) for _ in range(length))
    return password