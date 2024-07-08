from random import randint as rint


def attack1(num_defenders: int):
    attacker = rint(1, 6)
    defender = sum([rint(1, 6) if i == 0 else rint(1, 2) for i in range(num_defenders)])
    if attacker > defender:
        return True
    elif attacker < defender:
        return False
    else:
        return attack1(num_defenders)

def attack2(num_defenders: int):
    attacker = rint(1, 6)
    defender = sum([rint(1, 6) if i == 0 else 1 for i in range(num_defenders)])
    if attacker > defender:
        return True
    elif attacker < defender:
        return False
    else:
        return attack2(num_defenders)

def attack3(num_defenders: int):
    attacker = rint(1, 6)
    defender = sum([rint(1, 6) if i == 0 else 1 for i in range(num_defenders)])
    if attacker > defender:
        return True
    else:
        return False

