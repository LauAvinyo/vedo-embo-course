import vedo
import matplotlib.pyplot as matplt
import numpy as np

# Get point data
x = [1, 2, 3, 4, 5]
y = [4, 5, 2, 5, 4]

# Show with matplotlib
matplt.scatter(x, y)
matplt.show()
matplt.close()

# If you want to change the style of the points
# we have to modify the `scatter` plot.
matplt.scatter(x, y, color="#b22222")
matplt.show()
matplt.close()

# In Vedo, we create an object for the points
# and we add the ✨aesthetics✨ on the points object
pts = np.asarray(list(zip(x, y)))
points = vedo.Points(pts).c("#b22222").point_size(20)
vedo.show(points)
vedo.close()

# 🔥 Challenge: Can you add create a plot with a line in Vedo?
# Hint: Don't hesitate to check the documentation!
ln = np.asarray(list(zip(x, y)))
line = vedo.Line(ln).c("#22b2b2")
vedo.show(points, line)
vedo.close()
