from vedo import Mesh, dataurl, show

# load two meshes
limb1 = Mesh(dataurl + "270.vtk").c("gold")
limb2 = Mesh(dataurl + "290.vtk").c("red")

# align limb2 to limb1
aligned2 = limb2.clone().align_to(limb1).c("green5")

# compute the distance between the two meshes
aligned2.distance_to(limb1)
aligned2.cmap("Greens").add_scalarbar("residuals")

# show the meshes
show(limb1, limb2.wireframe(), aligned2, axes=1).close()
