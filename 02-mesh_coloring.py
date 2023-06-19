from vedo import dataurl, Plotter, Mesh

####################################
# Point coloring
man1 = Mesh(dataurl + "man_low.vtk")  # load a mesh

scals = man1.points()[:, 2] + 37  # pick z coordinates of vertices
man1.cmap("hot", scals, on="points")  # choose a colormap and colorize mesh points

#####################################
# Cell coloring
man2 = man1.clone()  # make a copy

scals = man2.cell_centers()[:, 2] + 37  # pick z coordinates of cells
man2.cmap("afmhot", scals, on="cells").add_scalarbar()

plt = Plotter(N=2, axes=11)  # create a 2x1 grid of subplots
plt.at(0).show(man1, "Colorize mesh points with scalars")
plt.at(1).show(man2, "Colorize mesh cells with scalars")
plt.interactive().close()  # close window when done
