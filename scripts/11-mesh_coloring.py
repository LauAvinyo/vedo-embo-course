from vedo import dataurl, Plotter, Mesh

####################################
# Point coloring
man1 = Mesh(dataurl + "man_low.vtk")  # load a mesh from file

scalars = man1.vertices[:, 2] + 37  # pick z coordinates of vertices
man1.cmap("afmhot", scalars, on="points")  # choose a colormap to colorize mesh points

#####################################
# Cell coloring
man2 = man1.clone()  # make an exact copy of man1

scalars = man2.cell_centers[:, 2] + 37  # pick z coordinates of cells
man2.cmap("afmhot", scalars, on="cells").add_scalarbar()

#####################################
# Create a 1x2 grid of subplots (1 row, 2 columns)
# axes=11 means: show a thin frame as a floor surface
plt = Plotter(shape=(1, 2), axes=11)
plt.at(0).show(man1, "Colorize mesh points with scalars")
plt.at(1).show(man2, "Colorize mesh cells with scalars\n(note the difference!)")
plt.interactive()  # allow user to rotate the scene
plt.close()  # close window when done
