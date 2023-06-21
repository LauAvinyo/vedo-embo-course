from vedo import Volume, dataurl
from vedo.applications import RayCastPlotter

vol = Volume(dataurl + "embryo.slc")
vol.mode(1).c("jet") # change appearance

plt = RayCastPlotter(vol, bg="blackboard", axes=7)
plt.show(viewup="z")
plt.close()
