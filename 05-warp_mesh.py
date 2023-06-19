"""Warp a region of a mesh using Thin Plate Splines.
Red points stay fixed while a single point in space
moves as the arrow indicates."""
from vedo import dataurl, Mesh, Arrows, Points, show

# load a mesh
mesh = Mesh(dataurl + "man.vtk").color("w")

# a heavily decimated copy with about 200 points
# (to speed up the computation)
meshdec = mesh.clone().triangulate().decimate(n=200)

sources = [[0.9, 0.0, 0.2]]  # this point moves
targets = [[1.2, 0.0, 0.4]]  # ...to this.
for pt in meshdec.points():
    if pt[0] < 0.3:  # these pts don't move
        sources.append(pt)  # (e.i. source = target)
        targets.append(pt)

# create the arrows
arrow = Arrows(sources, targets)

# create the points
apts = Points(sources).c("red")

# warp the mesh
warp = mesh.clone().warp(sources, targets)
warp.c("blue", 0.3).wireframe()

# show the mesh and the points
show(mesh, arrow, warp, apts, axes=1).close()
