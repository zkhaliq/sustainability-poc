import cx_Oracle

class OracleOperations:
    def __init__(self):
        self.hostname = "scan-prd-2101"
        self.port = "1541"
        self.service_name = "CSFPRD_SRVC_OTH.cisco.com"
        self.username = "XXCCS_EB_U"
        self.password = "********" 


    def establish_connection(self):
        dsn = cx_Oracle.makedsn(self.hostname, self.port, service_name=self.service_name)
        connection = cx_Oracle.connect(self.username, self.password, dsn)

        # Establish Oracle connection
        #connection = cx_Oracle.connect(connection_string)
        return connection


    def get_server_counts(self, guId):
        connection = self.establish_connection()
        cursor = connection.cursor()
        # Prepare and execute the SQL query
        sql_query = "SELECT /*+ PARALLEL(4) */ c.PRODUCT_FAMILY, count(1) FROM apps.xxccs_ds_instance_Detail a, apps.XXCCS_DS_SITE_GU_DENORM b, apps.XXCCS_DS_SAIB_ITEMS c WHERE a.item_name= c.item_name AND a.INSTALL_AT_SITE_USE_ID = b.SITE_USE_ID AND (INSTRB(c.DESCRIPTION, 'M3') > 0 OR INSTRB(C.DESCRIPTION, 'M4') > 0 ) AND c.PRODUCT_TYPE NOT IN('ACCESSORY', 'ASSEMBLY', 'BASE') AND c.PRODUCT_FAMILY IN('UCSC', 'UCSB') AND c.item_status_mfg NOT IN ('NONORD') AND C.PRODUCT_TYPE='SERVER' AND a.instance_status_id = 10000 AND b.gu_id = :gu_id GROUP BY c.PRODUCT_FAMILY"
        cursor.execute(sql_query, gu_id=guId)

        # Loop through the result set
        for row in cursor:
            productFamily = row[0]
            count = row[1]
    
            if 'UCSC' in productFamily:
                rack_quantity=count
                print("Rack Quantity: ",rack_quantity )
            else: 
                blade_quantity=count
                print("Blade Quantity: ",blade_quantity )

        cursor.close()
        connection.close()

        return rack_quantity, blade_quantity
