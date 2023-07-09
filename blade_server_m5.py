from blade_server import Blades
from adaptor_blade_m5m6 import AdaptorBladeM5M6
from memory_blade_m5 import MemoryBladeM5


class BladeServerM5(Blades):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.id = 29
        self.processorId = 1317
        self.processorTypeName = "Intel 8276 2.2GHz/165W 28C/38.50MB 3DX DDR4 2933 MHz"
        self.adaptor = [AdaptorBladeM5M6()]  # Assuming Adaptor is a class defined in the Adaptor module
        self.memory = [MemoryBladeM5()]  # Assuming Memory is a class defined in the Memory module