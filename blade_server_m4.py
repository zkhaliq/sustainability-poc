from blade_server import Blades
from adaptor_blade_m4 import AdaptorBladeM4
from memory_blade_m4 import MemoryBladeM4


class BladeServerM4(Blades):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.id = 27
        self.processorId = 997
        self.processorTypeName = "Intel E5-2640 v4 2.4 GHz/90W 10C/25MB Cache/DDR4 2133MHz"
        self.adaptor = [AdaptorBladeM4()]  # Assuming Adaptor is a class defined in the Adaptor module
        self.memory = [MemoryBladeM4()]  # Assuming Memory is a class defined in the Memory module