from rack_server import RackServer
from adaptor_rack_m4 import AdaptorRackM4
from memory_rack_m4 import MemoryRackM4


class RackServerM4(RackServer):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.id = 56
        self.powerSupplyId = 46      
        self.powerSupplyTypeName = "1200W PSU2V2"
        self.processorTypeName = "Intel E5-2640 v4 2.4 GHz/90W 10C/25MB Cache/DDR4 2133MHz"
        self.adaptor = [AdaptorRackM4()]  #  AdaptorRackM4 is a class 
        self.memory = [MemoryRackM4()]  #  Memory is a class
   
    # Add any specific methods or attributes for RackServerM5
