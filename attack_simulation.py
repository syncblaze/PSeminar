from typing import Callable, Type
from attack_functions import attack1, attack2, attack3

import matplotlib.pyplot as plt
import numpy as np

CASE = 4

attack: Type[Callable[[int], bool]]
attack2: Type[Callable[[int], bool]]

if CASE == 1:
    attack = attack1
elif CASE == 2:
    attack = attack2
elif CASE == 3:
    attack = attack3
elif CASE == 4:
    attack = attack2
    attack2 = attack3

res = {}

for i in range(1, 6):
    res[i] = {
        'win': 0,
        'lose': 0
    }
    for j in range(0, 100000):
        if attack(i):
            res[i]['win'] += 1
        else:
            res[i]['lose'] += 1
    res[i]['win_percent'] = res[i]['win'] / (res[i]['win'] + res[i]['lose']) * 100

if CASE == 4:
    res2 = {}
    for i in range(1, 6):
        res2[i] = {
            'win': 0,
            'lose': 0
        }
        for j in range(0, 100000):
            if attack2(i):
                res2[i]['win'] += 1
            else:
                res2[i]['lose'] += 1
        res2[i]['win_percent'] = res2[i]['win'] / (res2[i]['win'] + res2[i]['lose']) * 100


def create_bar_plot(ax, data, title):
    labels = data.keys()
    win_percentages = [data[label]['win_percent'] for label in labels]
    wins = [data[label]['win'] for label in labels]
    losses = [data[label]['lose'] for label in labels]

    ax.bar(labels, win_percentages, color='blue')
    ax.set_xlabel('Defenders')
    ax.set_ylabel('Probability to Win')
    ax.set_title(title, fontsize=10)
    ax.set_yticklabels(['{:.1f}%'.format(y) for y in ax.get_yticks()])


def create_two_bar_plot(ax, data, title):
    labels = data.keys()
    win_percentages = [data[label]['win_percent'] for label in labels]
    wins = [data[label]['win'] for label in labels]
    losses = [data[label]['lose'] for label in labels]
    bar_width = 0.35
    index = np.arange(len(labels))
    bar1 = ax.bar(index, wins, bar_width, label='Wins', color='blue')
    bar2 = ax.bar(index + bar_width, losses, bar_width, label='Losses', color='orange')

    ax.set_xlabel('Defenders')
    ax.set_ylabel('Number of Games')
    ax.set_title(title, fontsize=10)
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(labels)
    ax.legend()


if CASE != 4:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    create_bar_plot(ax1, res, "Probability to Win as Attacker with Different Number of Defenders")
    create_two_bar_plot(ax2, res, "Wins and Losses for Each Number of Defenders")
else:
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    fig.add_subplot(111, frame_on=False)
    plt.tick_params(labelcolor="none", top=False, bottom=False, left=False, right=False)

    create_bar_plot(axs[0, 0], res, "Probability to Win as Attacker with Different Number of Defenders")
    create_two_bar_plot(axs[0, 1], res, "Wins and Losses for Each Number of Defenders")

    fig.add_subplot(111, frame_on=False)
    plt.tick_params(labelcolor="none", top=False, bottom=False, left=False, right=False)

    create_bar_plot(axs[1, 0], res2,"Probability to Win as Attacker with Different Number\n of Defenders, which are standing on their own path")
    create_two_bar_plot(axs[1, 1], res2, "Wins and Losses for Each Number of Defenders,\n which are standing on their own path")

plt.tight_layout()
plt.savefig(f'attack_simulation_{CASE}.png', dpi=800)  # Adjust dpi as needed
plt.show()

print(res)
