import pygame as pg
from interactive_funcs import Button, Node, Edge
from algos import DFS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#function to visualize DFS
def visualize_DFS(traversal_order, screen):
    for node in traversal_order:
        node.color = RED
        pg.time.delay(1000)
        screen.fill(WHITE)
        for node in nodes:
            node.draw(screen)
        for edge in edges:
            edge.draw_edge(screen)
        pg.display.update()
    for node in traversal_order:
        node.color = GREEN


#basic initializers
pg.init()
screen_width = 1200
screen_height = 800
screen = pg.display.set_mode((screen_width, screen_height))
running = True

#add buttons
add_node_button = Button(50, 50, 150, 50, GREEN, "Add Node", BLACK)
add_edge_button = Button(50, 150, 150, 50, GREEN, "Add Edge", BLACK)
change_value_button = Button(50, 250, 150, 50, GREEN, "Change Value", BLACK)
DFS_button = Button(50, 350, 150, 50, GREEN, "DFS", BLACK)

#list of buttons
buttons = [add_node_button, add_edge_button, change_value_button, DFS_button]

#init lists for all nodes and edges
nodes = []
edges = []

#placeholder for dragged node and selected node
dragged_node = None
selected_node = None

#states
adding_edge = False
changing_value = False
selecting_start_node = False

while running == True:
    screen.fill(WHITE)

    #events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        #mouse events
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()

            #checking if mouse is over any button
            if add_node_button.is_over(pos):
                selecting_start_node, adding_edge, changing_value = False, False, False
                nodes.append(Node(len(nodes), len(nodes), 100, 100, GREEN))
            elif add_edge_button.is_over(pos):
                changing_value, selecting_start_node = False, False
                adding_edge = not adding_edge
            elif change_value_button.is_over(pos):
                adding_edge, selecting_start_node = False, False
                changing_value = not changing_value
            elif DFS_button.is_over(pos):
                adding_edge, changing_value = False, False
                if nodes:
                    selecting_start_node = True

            #checking if mouse is over any node
            else:
                for node in nodes:
                    if node.is_over(pos):

                        #adding edge
                        if adding_edge:
                            #set initial node
                            if selected_node == None:
                                selected_node = node
                            #set final node
                            else:
                                edges.append(Edge(selected_node, node))
                                selected_node = None
                                adding_edge = False
                                break

                        #changing value
                        elif changing_value:
                            node.value = int(input("Enter new value: "))
                            changing_value = False
                            break
                        
                        #DFS
                        elif selecting_start_node:
                            traversal_order = DFS(node)
                            visualize_DFS(traversal_order, screen)
                            selecting_start_node = False
                            break

                        #dragging node
                        else:
                            dragged_node = node
                            break
        #mouse up event to clear
        if event.type == pg.MOUSEBUTTONUP:
            dragged_node = None
        #mouse motion event to drag node
        if event.type == pg.MOUSEMOTION:
            if dragged_node != None:
                pos = pg.mouse.get_pos()
                dragged_node.x = pos[0]
                dragged_node.y = pos[1]


    #Drawing All nodes  
    for node in nodes:
        node.draw(screen)

    #drawwing edges
    for edge in edges:
        edge.draw_edge(screen)

    #drawing buttons
    for button in buttons:
        button.draw(screen)

    pg.display.update()
    

pg.quit()

