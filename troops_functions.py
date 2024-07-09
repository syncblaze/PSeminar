from random import randint as rint



def place_troops1(num_dice_rolls: int):
    dice_rolls = [rint(1, 6) for _ in range(num_dice_rolls)]
    if dice_rolls.count(6) == 4:
        return True
    else:
        return False

def place_troops2(num_dice_rolls: int):
    dice_rolls = [rint(1, 6) for _ in range(num_dice_rolls)]
    if dice_rolls.count(6) >= 4:
        return True
    else:
        return False

def place_troops3(num_dice_rolls: int):
    from math import comb

    n = num_dice_rolls
    p = 1 / 6

    cumulative_probability = comb(n, 4) * (p ** 4) * ((1 - p) ** (n - 4))

    return cumulative_probability

def place_troops4(num_dice_rolls: int):
    from math import comb

    n = num_dice_rolls
    p = 1 / 6

    cumulative_probability = 0

    # Berechnen der Wahrscheinlichkeit für jeden möglichen Erfolg von 4 bis 24
    for i in range(4, n + 1):
        # Berechnen der Wahrscheinlichkeit für genau i Erfolge
        probability_i = comb(n, i) * (p ** i) * ((1 - p) ** (n - i))

        # Addieren der berechneten Wahrscheinlichkeit zur kumulativen Wahrscheinlichkeit
        cumulative_probability += probability_i

    return cumulative_probability
