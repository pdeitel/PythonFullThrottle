# RollDie.py
"""Graphing frequencies of die rolls with Matplotlib."""
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

n_rolls = int(sys.argv[1])  # get number of rolls from command line 
rolls = random.choices(range(1, 7), k=n_rolls)  # roll the dice
faces, frequencies = np.unique(rolls, return_counts=True)  # summarize 

figure, axes = plt.subplots()  # get a window and its plot area
bars = axes.bar(faces, frequencies)  # create bar plot and get its bars

# add labels; scale y-axis by 15% to accommodate text at top of each bar
axes.set(title=f'Rolling a Six-Sided Die {n_rolls:,} Times',
    xlabel='Die Value', ylabel='Frequency',
    ylim=(0, frequencies.max() * 1.15))

# ensure large y-axis values display in fixed, not scientific, notation
axes.ticklabel_format(style='plain', axis='y') 

# label the bars with their frequencies
labels = [f'{f:,}\n{f / n_rolls:.3%}' for f in frequencies]
axes.bar_label(bars, labels=labels, padding=3)

plt.tight_layout()  
plt.show()  # display the Figure containing the bar plot




#**************************************************************************
#* (C) Copyright 1992-2026 by Deitel & Associates, Inc. and               *
#* Pearson Education, Inc. All Rights Reserved.                           *
#*                                                                        *
#* DISCLAIMER: The authors and publisher of this book have used their     *
#* best efforts in preparing the book. These efforts include the          *
#* development, research, and testing of the theories and programs        *
#* to determine their effectiveness. The authors and publisher make       *
#* no warranty of any kind, expressed or implied, with regard to these    *
#* programs or to the documentation contained in these books. The authors *
#* and publisher shall not be liable in any event for incidental or       *
#* consequential damages in connection with, or arising out of, the       *
#* furnishing, performance, or use of these programs.                     *
#**************************************************************************
