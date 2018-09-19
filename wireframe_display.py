import wireframe
import pygame

key_to_function = {
    pygame.K_LEFT: (lambda x: x.translateAll('x', -10)),
    pygame.K_RIGHT: (lambda x: x.translateAll('x', 10)),
    pygame.K_DOWN: (lambda x: x.translateAll('y', 10)),
    pygame.K_UP: (lambda x: x.translateAll('y', -10)),
    pygame.K_i: (lambda x: x.scaleAll(1.25)),
    pygame.K_o: (lambda x: x.scaleAll(0.8)),
    pygame.K_q: (lambda x: x.rotateAll('X', 0.1)),
    pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
    pygame.K_a: (lambda x: x.rotateAll('Y', 0.1)),
    pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
    pygame.K_z: (lambda x: x.rotateAll('Z', 0.1)),
    pygame.K_x: (lambda x: x.rotateAll('Z', -0.1))}


class ProjectionViewer:
    """Displays 3D Objects on a pygame screen"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Wireframe Display")
        self.background = (10,10,50)

        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.nodeRadius = 4

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        key_to_function[event.key](self)
            self.display()
            pygame.display.flip()

    def addWireframe(self, name, wire):
        self.wireframes[name] = wire

    def display(self):
        """Draw the wireframes on the screen"""

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen, self.edgeColour, (edge.start.x, edge.start.y), (edge.stop.x, edge.stop.y), 1)
            if self.displayNodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)

    def translateAll(self, axis, d):
        """With this, we can move the camera of the screen (all the objects are translating)"""

        for wireframe in self.wireframes.values():
            wireframe.translate(axis,d)

    def scaleAll(self, scale):
        """With this, we can zoom in/out the camera ( all the objects are scaling)"""

        for wireframe in self.wireframes.values():
            wireframe.scale(self.width/2, self.height/2, scale)


    def rotateAll(self, axis, theta):
        rotateFunction = "rotate" + axis

        for wireframe in self.wireframes.values():
            centre = wireframe.findCentre()
            getattr(wireframe, rotateFunction)(centre[0],centre[1],centre[2],theta) # esto es top del top
            #pilla la funcion con el getattr y le mete los argumentos

if __name__ == "__main__":
    cube = wireframe.Wireframe()
    cube.addNodes([(x, y, z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])
    cube.addEdges([(x, x + 4) for x in range(0, 4)] + [(x, x + 1) for x in range(0, 8, 2)] + [(x, x + 2) for x in (0, 1, 4, 5)])

    #cube2 = wireframe.Wireframe()
    #cube2.addNodes([(x, y, z) for x in (350, 10) for y in (10, 150) for z in (50, 250)])
    #cube2.addEdges(
    #    [(x, x + 4) for x in range(0, 4)] + [(x, x + 1) for x in range(0, 8, 2)] + [(x, x + 2) for x in (0, 1, 4, 5)])

    pv = ProjectionViewer(400,300)
    pv.addWireframe("cube", cube)
    #pv.addWireframe("cube2", cube2)
    pv.run()