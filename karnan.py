import re
def check(pwd):
    if (len(pwd) >= 8 and
        re.search(r"[A-Z]", pwd) and
        re.search(r"[a-z]", pwd) and
        re.search(r"[0-9]", pwd) and
        re.search(r"[!@#$%^&*]", pwd)):
        return "Strong"
    return "Weak"
print(check(input("Enter password: ")))
