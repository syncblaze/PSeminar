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


