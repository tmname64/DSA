from interactive_funcs import Button, Node, Edge
import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def DFS(start_node):
    stack = [start_node]
    visited = set()
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in node.edges:
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

def BFS(start_node):
    #Need to change it to use a real queue but i dont really want to rn
    queue = [start_node]
    visited = set()
    traversal_order = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in node.edges:
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal_order
