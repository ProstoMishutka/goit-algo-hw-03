import re

def normalize_phone(phone_number):
    pattern = r"[^\d+]"
    number = re.sub(pattern, "", phone_number)
    if "+38" not in number:
        return "+38" + number
    elif "+" not in number:
        return "+" + number
    else:
        return number
    
print(normalize_phone("067\\t123 4567"))
