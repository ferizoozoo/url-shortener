import random
import string

def code_generator(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))