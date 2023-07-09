from rack_server import RackServer
from adaptor_rack_m5 import AdaptorRackM5
from memory_rack_m5 import MemoryRackM5

class RackServerM5(RackServer):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.id = 33
        self.powerSupplyId = 16
        self.powerSupplyTypeName = "1600W PSU1"
        self.processorTypeName = "Intel 5220R 2.2GHz/150W 24C/35.75MB DCP DDR4 2666MHz"
        self.adaptor = [AdaptorRackM5()]  #  AdaptorRackM5 is a class 
        self.memory = [MemoryRackM5()]  #  MemoryRackM5 is a class
        self.processorId = 1339

        
    # Add any specific methods or attributes for RackServerM5
