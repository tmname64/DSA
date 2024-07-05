import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(self, x, y, width, height, color, text, text_color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pg.font.Font(None, 32)
        text = font.render(self.text, True, self.text_color)
        screen.blit(text, (self.x + self.width/2 - text.get_width()/2, self.y + self.height/2 - text.get_height()/2))

    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Node:
    def __init__(self, id, value, x, y, color) -> None:
        self.value = value
        self.x = x
        self.y = y
        self.color = color
        self.radius = 20
        self.edges = []

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        font = pg.font.Font(None, 32)
        text = font.render(str(self.value), True, BLACK)
        screen.blit(text, (self.x - text.get_width()/2, self.y - text.get_height()/2))

    def is_over(self, pos):
        if ((pos[0] - self.x)**2 + (pos[1] - self.y)**2)**0.5 < self.radius:
            return True
        return False
    

class Edge:
    def __init__(self, node1, node2, color = BLACK) -> None:
        self.node1 = node1
        self.node2 = node2
        self.color = color
        node1.edges.append(node2)
        node2.edges.append(node1)

    def draw_edge(self, screen):
        pg.draw.line(screen, self.color, (self.node1.x, self.node1.y), (self.node2.x, self.node2.y), 5)
