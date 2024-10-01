import random

def get_numbers_ticket(min, max, quantity):
    try:
        list_numbers = []
        random_numbers = []
        differ_number = (max + 1) - min  
        if min >= 1 and max <= 1000 and quantity <= differ_number:  
            for num in range(min, max + 1):
                list_numbers.append(num)
            random_numbers = random.sample(list_numbers, quantity)
            random_numbers.sort()
            return random_numbers
        else:
            return list_numbers
    except TypeError:
        print("The data is incorrect.")


print(get_numbers_ticket(1, 49, 6))