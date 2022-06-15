import random
import string

def Generate_URL():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits

    total = upper + lower + digits
    generate = random.sample(total, 7)

    result = "".join(generate)
    return result
