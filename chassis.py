from blade_server import Blades

class Chassis:
    def __init__(self, blades, index):
        self.id = 80
        self.quantity= "1"
        self.index = index
        self.hasValidConfig = True
        self.systemWorkloadPercent = 0
        self.redundancyMode = "N"
        self.inputVoltageId = 6
        self.powerSupplyId = 36
        self.powerSupplyTypeName = "2500W PSU DV"
        self.powerSupplyCount = 2
        self.iom = 801
        self.ioModuleTypeName = "2208"
        self.iomCount = 2
        self.blades = blades
        self.additionalComponentOne = None
        self.additionalComponentTwo = None
        self.additionalComponentThree = None
        self.additionalComponentFour = None
        self.additionalComponentFive = None
        self.projectName = "MayBankExisting"

