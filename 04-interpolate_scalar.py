from vedo import np, dataurl, Mesh, Points, show

# load a mesh
mesh = Mesh(dataurl + "bunny.obj")

# pick 100 points where we assume that some scalar value is known
pts2 = mesh.points()[:100]

# assume the value is random
scalars = np.random.randint(45, 123, 100)

# create a set fo points with this scalar values
points = Points(pts2, r=10).cmap("rainbow", scalars)

# interpolate from points onto the mesh, by averaging the 5 closest ones
mesh.interpolate_data_from(points, n=5).cmap("rainbow").add_scalarbar()

# show the mesh and the points
show(mesh, points).close()
