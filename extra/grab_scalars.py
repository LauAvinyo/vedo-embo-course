from vedo import Picture, settings, show
from vedo.applications import SplinePlotter

settings.default_backend = "vtk"

pic = Picture("data/sox9_exp.jpg").bw()

plt = SplinePlotter(pic)
plt.show(mode="image", zoom='tight')
outline = plt.line
plt.close()

print("Cutting with outline...")
msh = pic.tomesh().cmap("viridis_r")
cut_msh = msh.clone().cut_with_point_loop(outline)

cut_msh.interpolate_data_from(msh, n=3)
show(cut_msh, outline, axes=1).close()



