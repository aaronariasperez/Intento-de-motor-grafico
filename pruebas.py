from wireframe import *


wire = Wireframe()
wire.addNodes([(1, 2, 3), (1, 2, 1)])
wire.addEdges([(0, 1)])

wire.outputNodes()
wire.outputEdges()

print("\n **** New tests ****")

cube_nodes = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
cube = Wireframe()
cube.addNodes(cube_nodes)
cube.addEdges([(x, x+4) for x in range(0, 4)])
cube.addEdges([(x, x+1) for x in range(0, 8, 2)])
cube.addEdges([(x, x+2) for x in (0, 1, 4, 5)])
cube.outputNodes()
cube.outputEdges()
