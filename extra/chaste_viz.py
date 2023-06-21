from vedo import load
from vedo.applications import Browser
# Browser("data/chaste/Practical_2_3/results_*.vtu").show()

ugrids = load("data/chaste/Practical_2_3/results_*.vtu")

meshes = []
for u in ugrids:
    m = u.alpha(1).tomesh().linewidth(1)
    m.cmap("viridis_r", vmin=0.2, vmax=2)
    meshes.append(m)

Browser(meshes).show()

# ugrids = load("data/chaste/Practical_1_1/results_*.vtu")
# ugrids = load("data/chaste/Practical_1_2/results_*.vtu")
# ugrids = load("data/chaste/Practical_2_2/results_*.vtu")
# Browser("data/chaste/Practical_2_3/results_*.vtu").show()
