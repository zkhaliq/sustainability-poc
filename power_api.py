from rack_server import RackServer
from adaptor import Adaptor
from memory import Memory
from adaptor_blade import AdaptorBlade
from memory_blade import MemoryBlade
from blades import Blades
from chassis import Chassis
from sustainability_metrics import SustainbilityMetrics
import requests
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Adaptor, Memory, RackServer, Blades, Chassis, AdaptorBlade, MemoryBlade)):
            return obj.__dict__
        return super().default(obj)

def execute_post_api(json_data):
    headers = {'Content-Type': 'application/json','Authorization':'Basic ***'}
    url = "https://******/public/project/power"
    response = requests.post(url, data=json_data, headers=headers)
    response_json = response.json()
    return response_json

def build_api_payload(rack_quantity, bladeQuantity):
    # Set the quantity attribute
    rack_server = RackServer(rack_quantity)

    blade_quantity = min(bladeQuantity, 8)
    chassis_count = bladeQuantity // 8  # returns the quotient rounded down to the nearest whole number, this give X-1 number of chassis object to be created 
    #print(blade_quantity)
    #print(chassis_count)

    blades = []
    for i in range(chassis_count):
        blades.append(Blades(quantity=8))

    remaining_quantity = bladeQuantity % 8
    if remaining_quantity > 0:
        blades.append(Blades(quantity=remaining_quantity))

    chassis_list = []
    index = 0
    for blade in blades:
        index += 1
        chassis_list.append(Chassis(blade,index))    
    
    sustaibility_metrics = SustainbilityMetrics(rack_server, chassis_list)

    # Convert the RackServer object to JSON
    sustaibility_metrics_json = json.dumps(sustaibility_metrics.__dict__, cls=CustomEncoder)

    # Print the JSON representation
    #print(sustaibility_metrics_json)

    return sustaibility_metrics_json
 
