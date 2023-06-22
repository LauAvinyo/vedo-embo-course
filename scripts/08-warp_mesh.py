"""Warp a mesh (non-linear registration).
All points stay fixed while a single point in space
moves as the arrow indicates."""
from vedo import dataurl, Mesh, Arrows, show

# Load a mesh
mesh = Mesh(dataurl + "man.vtk").color("white")

# Create a heavily decimated copy with about 200 points
# (to speed up the computation)
mesh_dec = mesh.clone().triangulate().decimate(n=200)

sources = [[0.9, 0.0, 0.2]]  # this point moves
targets = [[1.2, 0.0, 0.4]]  # ...to this.
for pt in mesh_dec.points():
    if pt[0] < 0.3:  # while these pts don't move
        sources.append(pt)  # (e.i. source = target)
        targets.append(pt)

# Create the arrows representing the displacement
arrow = Arrows(sources, targets)

# Warp the mesh
mesh_warped = mesh.clone().warp(sources, targets)
mesh_warped.c("blue").wireframe()

# Show the meshes and the arrow
show(mesh, mesh_warped, arrow, axes=1)