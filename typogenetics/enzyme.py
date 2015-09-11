
from .base import Base
from .aminoacid import TertiaryDirection

class Enzyme:
    def __init__(self, acid_chain):
        self._acid_chain = acid_chain

    @property
    def acid_chain(self):
        return self._acid_chain

    @property
    def binding_preference(self):
        direction = self._determine_direction()
        return self._binding_base_by_direction(direction)

    def _binding_base_by_direction(self, direction):
        if direction == 0:
            return Base.adenine
        if direction == 1:
            return Base.cytozine
        if direction == 2:
            return Base.thymine
        if direction == 3:
            return Base.guanine

    def _determine_direction(self):
        direction_indicator = 0
        for acid in self._acid_chain:
            if acid.value.direction == TertiaryDirection.left:
                direction_indicator += 1
            elif acid.value.direction == TertiaryDirection.right:
                direction_indicator -= 1
        return direction_indicator % 4
