from adaptor import Adaptor
from memory import Memory
from rack_server import RackServer
from chassis import Chassis


class SustainbilityMetrics:
    def __init__(self, rackservers,chassis):
        self.projectName = "Bharti Airtel-Existing"
        self.rackServers = [rackservers]
        self.chassis = chassis
        self.invictaServers = []
        self.switches = []
        self.mseries = []
        self.additionalPlatform = []