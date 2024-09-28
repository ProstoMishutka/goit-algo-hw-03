import random

def get_numbers_ticket(min, max, quantity):
    while True:
        try:
            collec_unic_num = set(range(min, max+1))
            if min < 1 or max > 1000 or (min > quantity > max):
                print("The value entered is incorrect, please enter the minimum" \
                    "number, maximum number, and the quantity of numbers" \
                    "in the format: min, max, quantity.")
                min = int(input("Input min: "))
                max = int(input("Input max: "))
                quantity = int(input("Input quantity: "))
            else:
                random_nums = random.sample(list(collec_unic_num), quantity)
                sorted_list_nums = sorted(random_nums)
                return f"Ваші лотерейські числа: {sorted_list_nums}"
        
        except (TypeError, ValueError):
            print("The value entered is incorrect, please enter the minimum" \
                    "number, maximum number, and the quantity of numbers" \
                    "in the format: min, max, quantity.")
            min = int(input("Input min: "))
            max = int(input("Input max: "))
            quantity = int(input("Input quantity: "))

print(get_numbers_ticket(1, 1000, 99))