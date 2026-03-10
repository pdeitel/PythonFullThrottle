# RollDieDynamic.py
"""Dynamically graphing frequencies of die rolls."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random
import sys

def update(frame_number, rolls, faces, frequencies, axes):
    """Configures bar plot contents for each animation frame."""
    # roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randint(1, 6) - 1] += 1

    # reconfigure plot for updated die frequencies
    axes.cla()  # clear old contents of plot area
    bars = axes.bar(faces, frequencies)  # new bars
    
    # add labels; scale y-axis by 15% for text at top of each bar
    axes.set(title=f'Die Frequencies for {sum(frequencies):,} Rolls',
        xlabel='Die Value', ylabel='Frequency',
        ylim=(0, max(frequencies) * 1.15))

    # ensure y-axis values display in fixed, not scientific, notation
    axes.ticklabel_format(style='plain', axis='y')

    # label the bars with their frequencies
    labels = [f'{freq:,}\n{freq / sum(frequencies):.3%}' 
                 for freq in frequencies]
    axes.bar_label(bars, labels=labels, padding=3)
    plt.tight_layout()

# read command-line arguments for number of frames and rolls per frame
number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])

figure = plt.figure('Rolling a Six-Sided Die')  # Figure for animation
axes = figure.add_subplot()  # add an Axes object
values = list(range(1, 7))  # die faces for display on x-axis
frequencies = [0] * 6  # six-element list of die frequencies set to 0s

# configure and start animation that calls the function update
die_animation = animation.FuncAnimation(
   figure, update, repeat=False, frames=number_of_frames - 1, 
   interval=33, fargs=(rolls_per_frame, values, frequencies, axes))

plt.show()  # display window


##########################################################################
# (C) Copyright 1992-2026 by Deitel & Associates, Inc. and               #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
