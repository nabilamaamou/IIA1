from abc import ABC, abstractmethod

class Puerto(ABC):
    def __init__(self, slot):
        self.slot = slot

    def getSlot(self):
        return self.slot
