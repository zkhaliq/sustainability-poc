from adaptor_blade import AdaptorBlade
from memory_blade import MemoryBlade

class Blades:
    def __init__(self, quantity):
        self.id = 27
        self.chassisId = "80"
        self.quantity = quantity
        self.index = 0
        self.hasValidConfig = True
        self.systemWorkloadPercent = 50
        self.processorId = 997
        self.processorTypeName = "Intel E5-2640 v4 2.4 GHz/90W 10C/25MB Cache/DDR4 2133MHz"
        self.processorCount = "2"      
        self.dedicatedStorage = []
        self.storage = []
        self.adaptor = [AdaptorBlade()]  # Assuming Adaptor is a class defined in the Adaptor module
        self.memory = [MemoryBlade()]  # Assuming Memory is a class defined in the Memory module
        self.additionalComponentOne = None
        self.additionalComponentTwo = None
        self.additionalComponentThree = None
        self.additionalComponentFour = None
        self.additionalComponentFive = None
        self.projectName = "Bharti Airtel-Existing"

