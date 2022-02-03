import matplotlib.pyplot as plt
import numpy as np
import pandas

x_position1 = [2,3]
x_position2 = [3,4]
x_position3 = [1,4]

plt.plot(x_position1, [1,1], 'o-')
plt.plot(x_position2, [2,2], 'o-')
plt.plot(x_position3, [3,3], 'o-')

plt.text(x_position1[0],1.2, 'Restriction 1')
plt.text(x_position2[0],2.2, 'Restriction 2')
plt.text(x_position3[0],3.2, 'Restriction 3')

plt.xlim(0,5)
plt.ylim(0,4)

ax = plt.gca()
ax.axes.yaxis.set_visible(False)

plt.title('Government Policy')

plt.show()


print('Hello')
