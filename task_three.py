import re

def normalize_phone(phone_number):
    pattern = r"[^\d+]"
    number = re.sub(pattern, "", phone_number)
    if number.startswith("38"):
        return "+" + number
    elif not number.startswith("+38"):
        return "+38" + number
    else:
        return number
    
print(normalize_phone("067\\t123 4567"))
