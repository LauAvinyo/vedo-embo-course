from vedo import Image, settings, show
from vedo.applications import SplinePlotter

settings.default_backend = "vtk"

pic = Image("../data/sox9_data/sox9_exp.jpg").bw()

plt = SplinePlotter(pic)
plt.show(mode="image", zoom="tight")
outline = plt.line
plt.close()

# create a mesh from the image
msh = pic.tomesh()

print("Cutting using outline... (please wait)")
cut_msh = msh.clone().cut_with_point_loop(outline)
cut_msh.print()
cut_msh.pointdata.select("RGBA")
cut_msh.cmap("viridis_r").add_scalarbar3d("Sox9 Level")

show(cut_msh, outline, axes=1).close()
