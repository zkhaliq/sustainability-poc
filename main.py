from oracle_operations import OracleOperations
from power_api import build_api_payload, execute_post_api
from generateInsights import generateInsights
from recoRuleEngine import recoRuleEngine
from upload_s3 import S3Uploader


if __name__ == '__main__':
    rack_quantity_value = 229
    bladeQuantity = 12
    gu_id = 96361

    oracle_ops = OracleOperations()
    #rack_quantity_value, bladeQuantity = oracle_ops.get_server_counts(gu_id)

    sustaibility_metrics_json = build_api_payload(rack_quantity_value, bladeQuantity)
    response_json = execute_post_api(sustaibility_metrics_json)

    # Extract and round off metricCoolingWatts and imperialCooling values
    input_cooling = response_json['inputCooling']
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
    gi.totalproduct["oldSeriesknt"] = rule_engine.asisConfig["bServer"] + rule_engine.asisConfig["rServer"]
    gi.totalproduct["oldChassisknt"] = round(rule_engine.asisConfig["bServer"] / 8)
    gi.totalproduct["newSeriesknt"] = rule_engine.recommendedConfig["bServer"]
    gi.totalproduct["newChassisknt"] = rule_engine.recommendedConfig["chassis"]
    gi.runInsights()
    
    insightsData = gi.response 
    print(gi.response)

     # Instantiate S3Uploader with your bucket name
    s3_uploader = S3Uploader()

    # Upload the JSON file to S3
    file_name = f"{gu_id}.json"
    s3_uploader.upload_json_file(file_name, insightsData)