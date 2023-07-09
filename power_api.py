from memory_rack_m4 import MemoryRackM4
from memory_rack_m5 import MemoryRackM5
from memory_blade_m4 import MemoryBladeM4
from memory_blade_m5 import MemoryBladeM5
from memory_blade_m6 import MemoryBladeM6

from adaptor_rack_m4 import AdaptorRackM4
from adaptor_rack_m5 import AdaptorRackM5
from adaptor_blade_m4 import AdaptorBladeM4
from adaptor_blade_m5m6 import AdaptorBladeM5M6

from rack_server_m4 import RackServerM4
from rack_server_m5 import RackServerM5

from blade_server_m4 import BladeServerM4
from blade_server_m5 import BladeServerM5
from blade_server_m6 import BladeServerM6
from blade_server_m7 import BladeServerM7


from blade_server import Blades
from rack_server import RackServer

from switches import Switches
from chassis import Chassis
from power_api_request import PowerAPIRequest

import requests
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (MemoryRackM4, MemoryRackM5, MemoryBladeM4, MemoryBladeM5, MemoryBladeM6,
         AdaptorRackM4, AdaptorRackM5, AdaptorBladeM4, AdaptorBladeM5M6, RackServerM4, RackServerM5, 
         BladeServerM4, BladeServerM5, BladeServerM6, Blades, RackServer, Switches, Chassis, PowerAPIRequest  )):
            return obj.__dict__
        return super().default(obj)

def execute_post_api(json_data):
    headers = {'Content-Type': 'application/json','Authorization':'Basic dWNzX3VzZXI6dWNzX3Bhc3N3b3Jk'}
    url = "https://ucsngws.cisco.com/public/project/power"
    response = requests.post(url, data=json_data, headers=headers)
    response_json = response.json()
    return response_json

def build_api_payload(counts):
    rackservers = []
    chassis_list = []

    # Initialize RackServers with Quantity. RackServers don't need Chassis
    if counts.rack_m4_servers > 0:
        rackserver_m4 = RackServerM4(counts.rack_m4_servers)
        rackservers.append(rackserver_m4)

    if counts.rack_m5_servers > 0:
        rackserver_m5 = RackServerM5(counts.rack_m5_servers)
        rackservers.append(rackserver_m5)

    # Chassis
    chassis_index = 1
    blade_server_types = [
        (BladeServerM4, counts.blade_m4_servers),
        (BladeServerM5, counts.blade_m5_servers),
        (BladeServerM6, counts.blade_m6_servers),
        (BladeServerM7, counts.blade_m7_servers)
    ]

    chassis_blades = []  # List to hold the blades for a single chassis

    for blade_server_type, server_count in blade_server_types:
        while server_count > 0:
            remaining_capacity = 8 - sum(b.quantity for b in chassis_blades)
            if remaining_capacity == 0:
                # If the current chassis is full, create a new chassis and reset the list
                chassis_list.append(Chassis(chassis_blades, chassis_index))
                chassis_index += 1
                chassis_blades = []
                remaining_capacity = 8

            # Determine the quantity to add to the current chassis
            blade_quantity = min(server_count, remaining_capacity)
            if blade_quantity > 0:
                chassis_blades.append(blade_server_type(quantity=blade_quantity))

            server_count -= blade_quantity

    # Add the remaining blades to the last chassis
    if chassis_blades:
        chassis_list.append(Chassis(chassis_blades, chassis_index))

    switches = []
    powerapi_request = PowerAPIRequest(rackservers, chassis_list, switches)

    # Convert the RackServer object to JSON
    powerapi_request_json = json.dumps(powerapi_request.__dict__, cls=CustomEncoder)

    # Print the JSON representation
    print(powerapi_request_json)

    return powerapi_request_json



 

