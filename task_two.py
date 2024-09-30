import random

def get_numbers_ticket(min, max, quantity):
    try:
        list_numbers = []
        random_numbers = []
        if min >= 1 and max <= 1000 and min <= quantity <= max:
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