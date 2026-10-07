import re

emails = ["an@email.com", "BINH@EMAIL.VN", "invalid", "cuong@"]


def validEmail(emailStr: str):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pattern, emailStr.lower()):
        return True
    return False


for eml in emails:
    if validEmail(eml):
        print(f"Email hợp lệ: {eml}")
    else:
        print(f"Email không hợp lệ: {eml}")
