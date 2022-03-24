import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

with open('./timeline.txt') as file:
    dates, names = zip(*[line.split(maxsplit=1) for line in file])

dates = [datetime.strptime(d, "%Y") for d in dates]

# Choose some nice levels
levels = np.tile([5, 3, 1], int(np.ceil(len(dates)/3)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
# ax.set(title="Amide activation breakthroughs")

ax.vlines(dates, 0, levels, color="#E69F00")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="none", markeredgecolor='none',
        markerfacecolor="#E69F00")  # Baseline and markers on it.

# annotate lines
# for d, l, r in zip(dates, levels, names):
#     ax.annotate(r, xy=(d, l),
#                 xytext=(-3, np.sign(l)*3), textcoords="offset points",
#                 horizontalalignment="right",
#                 verticalalignment="bottom" if l > 0 else "top")

# format xaxis with 4 month intervals
ax.get_xaxis().set_major_locator(mdates.YearLocator(10))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y axis and spines
ax.get_yaxis().set_visible(False)
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False)

ax.margins(y=0.1)
plt.savefig("timeline.png")
plt.savefig("timeline.svg")
