from typing import Callable, Type

import numpy as np
from matplotlib import pyplot as plt

from troops_functions import place_troops1, place_troops2, place_troops3, place_troops4

CASE = 2
ADD_CALCULATION = True

if CASE == 1:
    place_troops = place_troops1
    place_troops_calc = place_troops3
elif CASE == 2:
    place_troops = place_troops2
    place_troops_calc = place_troops4


res = {}

for i in range(1,70):
    res[i] = {
        'win': 0,
        'lose': 0
    }
    print("Simulating", i)
    for j in range(0, 100000):
        if place_troops(i):
            res[i]['win'] += 1
        else:
            res[i]['lose'] += 1
    if ADD_CALCULATION:
        print("Calculating", i)
        res[i]['win_percent_calc'] = float(place_troops_calc(i)) * 100
    res[i]['win_percent'] = res[i]['win'] / (res[i]['win'] + res[i]['lose']) * 100


labels = res.keys()
labels_list = list(labels)
win_percentages = [res[label]['win_percent'] for label in labels]
if ADD_CALCULATION:
    win_percentages_calc = [res[label]['win_percent_calc'] for label in labels]

# Sort labels and win_percentages
sorted_indices = np.argsort(labels_list)
labels_list_sorted = np.array(labels_list)[sorted_indices]
win_percentages_sorted = np.array(win_percentages)[sorted_indices]

fig, ax1 = plt.subplots(1, 1, figsize=(14, 6))
if ADD_CALCULATION:
    bars = ax1.bar(labels_list, win_percentages_calc, label=r'$P(x=4)$', linewidth=1, edgecolor='black', width=1)


ax1.plot(labels_list_sorted, win_percentages_sorted, label=r'$P(x=4) (Simulation)$' if CASE % 2 == 0 else r'$P(x\geq4) (Simulation)$', color='red' if ADD_CALCULATION else 'blue')
ax1.set_title(f"Probability of placing 4{'or more Troops' if CASE % 2 == 0 else ' Troops'}")
ax1.set_xlabel("Number of dice")
ax1.set_ylabel("Win percentage")

# Adjust y-tick positions
ytick_positions = np.linspace(0, 100 if CASE % 2 == 0 else 25, 21)  # You can adjust the number of ticks
ax1.set_yticks(ytick_positions)
ax1.set_yticklabels(['{:.1f}%'.format(y) for y in ytick_positions])

# Draw grid lines
ax1.grid(axis='y', linestyle='--', alpha=0.7)

if CASE % 2 != 0:
    ax1.axvline(x=24, color='red', linestyle='--', label=r'$E(X) = n \cdot \frac{1}{6} = 4 \Rightarrow n = 24$', ymin=0, ymax=1)

ax1.set_xticks(labels_list_sorted[::2])
ax1.set_xticklabels(labels_list_sorted[::2])

plt.legend()
plt.savefig(f'troop_simulation_{CASE if not ADD_CALCULATION else f"{CASE}_calc"}.png', dpi=800)  # Adjust dpi as needed
plt.show()

