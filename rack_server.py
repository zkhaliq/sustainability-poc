from adaptor import Adaptor
from memory import Memory

class RackServer:
    def __init__(self, quantity):
        self.id= 56
        self.quantity = quantity
        self.index = 1
        self.hasValidConfig = True
        self.systemWorkloadPercent = 50
        self.redundancyMode = "N"
        self.inputVoltageId = 6
        self.powerSupplyId = 46      
        self.powerSupplyTypeName = "powersupply"
        self.powerSupplyCount = 2
        self.mezzanineControllerId = None
        self.mezzanineControllerTypeName = ""
        self.mezzanineControllerCount = 0
        self.dedicatedStorage = []
        self.storage = []
        self.adaptor = [Adaptor()]  # Assuming Adaptor is a class defined in the Adaptor module
        self.memory = [Memory()]  # Assuming Memory is a class defined in the Memory module
        self.processorId = 997
        self.processorTypeName = "Intel E5-2640 v4 2.4 GHz/90W 10C/25MB Cache/DDR4 2133MHz"
        self.processorCount = "2"
        self.additionalComponentOne = None
        self.additionalComponentTwo = None
        self.additionalComponentThree = None
        self.additionalComponentFour = None
        self.additionalComponentFive = None
        self.projectName = "Bharti Airtel-Existing"
