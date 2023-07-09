from blade_server import Blades
from adaptor_blade_m5m6 import AdaptorBladeM5M6
from memory_blade_m6 import MemoryBladeM6


class BladeServerM6(Blades):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.id = 16
        self.processorId = 1271
        self.processorTypeName = "Intel 5320 2.20GHz/185W 26C/39MB Cache/DDR4 2933MHz"
        self.adaptor = [AdaptorBladeM5M6()]  # Assuming Adaptor is a class defined in the Adaptor module
        self.memory = [MemoryBladeM6()]  # Assuming Memory is a class defined in the Memory module

