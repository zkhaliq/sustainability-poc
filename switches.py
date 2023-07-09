class Switches:
    def __init__(self, quantity, ports, index):
        self.id= 3
        self.quantity = quantity
        self.index = index
        self.activePorts = ports
        self.hasValidConfig = True
        self.redundancyMode = "N"
        self.inputVoltageId = 6
        self.powerSupplyId = 32     
        self.powerSupplyTypeName = "750W PSU"
        self.powerSupplyCount = 2
        self.expansionCards = []
        self.projectName = "Bharti Airtel-Existing"
        self.systemWorkloadPercent = 50