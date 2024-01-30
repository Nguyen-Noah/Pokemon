import pygame, random
from utils.elements import Element
from .pokedex import Pokedex

class Trainer(Element):
    def __init__(self, type, controller):
        super().__init__()
        self.type = type
        self.pokedex = Pokedex(self)
        self.render_pokemon = False
        self.potions = random.randint(0, 4)

        self.controller = controller
        if self.controller not in ['player', None]:
            self.controller = controller(self)

    @property
    def active_pokemon(self):
        return self.pokedex.team_pokemon[0]

    def add_pokemon(self, pokemon):
        self.pokedex.add(pokemon)

    def use_potion(self):
        if self.potions:
            self.potions -= 1
            self.active_pokemon.heal(10)

    def update(self):
        self.pokedex.update()

        if self.controller not in ['player', None]:
            self.controller.update()

    def render(self, surf):
        pass
