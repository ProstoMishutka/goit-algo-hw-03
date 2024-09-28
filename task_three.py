import re

def normalize_phone(phone_number):
    list_numbers = []
    for num in phone_number:
        pat_one = r"[^\d+]"
        delet_symb = re.sub(pat_one, "", num)
        
        if  not re.match(r"^\+380", delet_symb):
            if not re.match(r"^380", delet_symb):
                delet_symb = "+38" + delet_symb
            else:
                delet_symb = "+" + delet_symb
            list_numbers.append(delet_symb)
        else:
            list_numbers.append(delet_symb)
    return f"Нормалізовані номери телефонів для SMS-розсилки: {list_numbers}"

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
print(normalize_phone(raw_numbers))
