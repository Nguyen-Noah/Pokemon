import pygame
from .entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.money = 0
        