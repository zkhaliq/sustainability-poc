from oracle_operations import OracleOperations
from power_api import build_api_payload, execute_post_api
from generateInsights import generateInsights
from recoRuleEngine import recoRuleEngine
from upload_s3 import S3Uploader
from json_to_pdf import JSONtoPDFConverter
from server_counts import ServerCounts
import json

if __name__ == '__main__':

    counts = ServerCounts(12, 5, 0, 105, 67, 22, 0)
    gu_id = 145889241 #145889241 #96361

    #oracle_ops = OracleOperations()
    #rack_quantity_value, bladeQuantity = oracle_ops.get_server_counts(gu_id)
    
    powerapi_request_json = build_api_payload(counts)
    powerapi_response_json= execute_post_api(powerapi_request_json)

    print(powerapi_response_json)

    # Extract and round off metricCoolingWatts and imperialCooling values
    input_cooling = powerapi_response_json['inputCooling']
    metric_cooling_watts = round(input_cooling['metricCoolingWatts'])
    imperial_cooling = round(input_cooling['imperialCooling'])

    # Print the rounded-off values
    print("Metric Cooling Watts:", metric_cooling_watts, "W")
    print("Imperial Cooling:", imperial_cooling, "BTU/hr")

    # Create an instance of the recoRuleEngine class
    rule_engine = recoRuleEngine()

    # Set the values for asisConfig
    rule_engine.asisConfig["bServer"] = bladeQuantity
    rule_engine.asisConfig["rServer"] = rack_quantity_value

    # Run the rule to compute recommendedConfig
    rule_engine.runRule()

    # Calculate the number of FIs needed for the existing config
    rule_engine.calcFI()

    # Print the recommendedConfig and asisConfig
    print("AS-IS Config:", rule_engine.asisConfig)
    print("Recommended Config:", rule_engine.recommendedConfig)

    recommended_metrics_json = build_api_payload(0, rule_engine.recommendedConfig["bServer"])
    recommended_res_json = execute_post_api(recommended_metrics_json)

    # Extract and round off metricCoolingWatts and imperialCooling values
    recommended_input_cooling = recommended_res_json['inputCooling']
    rec_metric_cooling_watts = round(recommended_input_cooling['metricCoolingWatts'])
    rec_imperial_cooling = round(recommended_input_cooling['imperialCooling'])

    # Print the rounded-off values
    print("After Recommendation, Metric Cooling Watts:", rec_metric_cooling_watts, "W")
    print("After Recommendation, Imperial Cooling:", rec_imperial_cooling, "BTU/hr")

    gi = generateInsights()
    gi.totalProduct["oldSeriesknt"] = rule_engine.asisConfig["bServer"] + rule_engine.asisConfig["rServer"]
    gi.totalProduct["oldChassisknt"] = round(rule_engine.asisConfig["bServer"] / 8)
    gi.totalProduct["newSeriesknt"] = rule_engine.recommendedConfig["bServer"]
    gi.totalProduct["newChassisknt"] = rule_engine.recommendedConfig["chassis"]
    
    gi.asisSustainabilityParams["Power"] = metric_cooling_watts
    gi.newSustainabilityParams["Power"] = rec_metric_cooling_watts
    gi.asisSustainabilityParams["heat"] = imperial_cooling
    gi.newSustainabilityParams["heat"] = rec_imperial_cooling
    gi.runInsights()
    
    insightsData = gi.response 
    print("Insights for GUID :", gu_id)
    print(gi.response)

     # Instantiate S3Uploader with your bucket name
    s3_uploader = S3Uploader()

    # Upload the JSON file to S3
    file_name = f"{gu_id}.json"
    s3_uploader.upload_json_file(file_name, insightsData)

    #infoFromJson = json.loads(insightsData)
    #print(json2html.convert(insightsData))

    converter = JSONtoPDFConverter()
    converter.convert_json_to_pdf(insightsData)



    # Now you can upload the PDF content to S3
    # Upload code goes here