def password():
    import random

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    numbers = "0123456789"
    password = ""
    all = lower + upper + numbers
    r = random.sample(all, 9)
    for i in r: password += i
    return password