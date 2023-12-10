# importing libraries
# import matplotlib.pyplot as plt
# import numpy as np
# import math
#
# # Get the angles from 0 to 2 pie (360 degree) in narray object
# X = [2, 3, 4, 5]
#
# # Using built-in trigonometric function we can directly plot
# # the given cosine wave for the given angles
# Y1 = np.sin(X)
# Y2 = np.cos(X)
# Y3 = np.tan(X)
#
# # Initialise the subplot function using number of rows and columns
# figure, axis = plt.subplots(3, 1)
#
# # For Sine Function
# axis[0].bar(X, Y1)
# axis[0].set_title("Accuracy")
#
# # For Cosine Function
# axis[1].bar(X, Y2)
# axis[1].set_title("Precision")
#
# # For Tangent Function
# axis[2].bar(X, Y3)
# axis[2].set_title("Recall")
#
# # Combine all the operations and display
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# set width of bars
barWidth = 0.25

figure, axis = plt.subplots(3, 1)

# set heights of bars
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]

accours = [99, 99, 98, 98]
acctrad = [99, 99, 98, 98]
recallours = [98, 98, 98, 98]
recalltrad = [98, 98, 98, 98]
precisionours = [99, 98, 99, 98]
precisiontrad = [99, 98, 99, 98]
# Set position of bar on X axis
r1 = [2, 3, 4, 5]
print(r1)
r2 = [x + barWidth for x in r1]

# Make the plot
axis[0].bar(r1, accours, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
axis[0].bar(r2, acctrad, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
axis[1].bar(r1, recalltrad, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
axis[1].bar(r2, recallours, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
axis[2].bar(r1, precisiontrad, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')
axis[2].bar(r2, precisionours, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')

# Add xticks on the middle of the group bars
# plt.xlabel('group', fontweight='bold')
# plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
#
# # Create legend & Show graphic
# plt.legend()
plt.show()
