import math

class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class Wireframe:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def addNodes(self, nodeList):
        for node in nodeList:
            self.nodes.append(Node(node))
    def addEdges(self, edgeList):
        for (start, stop) in edgeList:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))
    def outputNodes(self):
        print("\n --- Nodes ---")
        for i, node in enumerate(self.nodes):
            print(" %d: (%.2f, %.2f, %.2f)" % (i, node.x, node.y, node.z))

    def outputEdges(self):
        print("\n --- Edges ---")
        for i, edge in enumerate(self.edges):
            print(" %d: (%.2f, %.2f, %.2f)" % (i, edge.start.x, edge.start.y, edge.start.z), end="")
            print(" to (%.2f, %.2f, %.2f)" % (edge.stop.x, edge.stop.y, edge.stop.z))

    def translate(self, axis, d):
        if axis in ["x", "y", "z"]:
            for node in self.nodes:
                setattr(node,axis,getattr(node,axis)+d) #setattr y getattr son muy top

    def scale(self, centre_x, centre_y, scale):
        """scale the wireframe from the point (centrex, centrey)"""

        for node in self.nodes:
            node.x = centre_x + scale * (node.x - centre_x)
            node.y = centre_y + scale * (node.y - centre_y)
            node.z *= scale

    def rotateZ(self, cx, cy, cz, radians):
        for node in self.nodes:
            x = node.x - cx
            y = node.y - cy
            d = math.hypot(y,x)
            theta = math.atan2(y,x) + radians
            node.x = cx + d*math.cos(theta)
            node.y = cy + d*math.sin(theta)

    def rotateX(self, cx, cy, cz, radians):
        for node in self.nodes:
            y = node.y - cy
            z = node.z - cz
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            node.z = cz + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)

    def rotateY(self, cx, cy, cz, radians):
        for node in self.nodes:
            x = node.x - cx
            z = node.z - cz
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            node.z = cz + d * math.cos(theta)
            node.x = cx + d * math.sin(theta)

    def findCentre(self):
        num_nodes = len(self.nodes)
        meanX = sum([node.x for node in self.nodes]) / num_nodes
        meanY = sum([node.y for node in self.nodes]) / num_nodes
        meanZ = sum([node.z for node in self.nodes]) / num_nodes

        return (meanX, meanY, meanZ)
