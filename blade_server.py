from adaptor_blade_m4 import AdaptorBladeM4
from memory_blade_m4 import MemoryBladeM4

class Blades:
    def __init__(self, quantity, index):
        self.id = 27
        self.chassisId = "80"
        self.quantity = quantity
        self.index = index
        self.hasValidConfig = True
        self.systemWorkloadPercent = 50
        self.processorId = 997
        self.processorTypeName = "Intel E5-2640 v4 2.4 GHz/90W 10C/25MB Cache/DDR4 2133MHz"
        self.processorCount = "2"      
        self.dedicatedStorage = []
        self.storage = []
        self.adaptor = [AdaptorBladeM4()]  # Assuming Adaptor is a class defined in the Adaptor module
        self.memory = [MemoryBladeM4()]  # Assuming Memory is a class defined in the Memory module
        self.additionalComponentOne = None
        self.additionalComponentTwo = None
        self.additionalComponentThree = None
        self.additionalComponentFour = None
        self.additionalComponentFive = None
        self.projectName = "MayBankExisting"

